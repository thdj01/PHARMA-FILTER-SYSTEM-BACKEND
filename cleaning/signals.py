# cleaning/signals.py

from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json

from .models import AuditLog
from filters.models import Filter, AHU, Plant
from users.models import User
from .middleware import get_request_details

# --- Helper Function ---
def log_audit_event(user, action, instance, old_values=None, new_values=None):
    """
    Creates an AuditLog entry. It now expects dictionaries that are already
    prepared for logging.
    """
    if not user or not user.is_authenticated:
        return
    
    _, ip, user_agent = get_request_details()

    # Use Django's built-in JSON encoder which handles dates, decimals, etc.
    # We dump and then load to ensure the data is in a pure JSON-compatible format.
    try:
        old_values_serializable = json.loads(json.dumps(old_values, cls=DjangoJSONEncoder)) if old_values else None
        new_values_serializable = json.loads(json.dumps(new_values, cls=DjangoJSONEncoder)) if new_values else None
    except TypeError:
        # Fallback if there's still a serialization issue
        old_values_serializable = {'error': 'Could not serialize old data'}
        new_values_serializable = {'error': 'Could not serialize new data'}


    AuditLog.objects.create(
        user=user,
        action=action,
        table_name=instance._meta.db_table,
        record_id=instance.pk,
        old_values=old_values_serializable,
        new_values=new_values_serializable,
        ip_address=ip,
        user_agent=user_agent
    )

# --- Signal Receivers for Model Auditing ---

AUDITED_MODELS = [Filter, AHU, Plant, User]

def get_changed_data(instance):
    """Helper to get old and new dictionary representations of a model instance."""
    new_values = model_to_dict(instance)
    old_values = {}
    if hasattr(instance, '_old_instance') and instance._old_instance is not None:
        old_values = model_to_dict(instance._old_instance)
    
    # Clean up password field for security
    if 'password' in new_values:
        new_values['password'] = '********'
    if 'password' in old_values:
        old_values['password'] = '********'
        
    return old_values, new_values

@receiver(pre_save, sender=Filter)
@receiver(pre_save, sender=AHU)
@receiver(pre_save, sender=Plant)
@receiver(pre_save, sender=User)
def cache_old_instance(sender, instance, **kwargs):
    """
    Before a model is saved, if it already exists, store its current state
    on the instance object itself.
    """
    if instance.pk:
        try:
            # Store a dictionary of the old instance
            instance._old_instance = sender.objects.get(pk=instance.pk)
        except sender.DoesNotExist:
            instance._old_instance = None

@receiver(post_save, sender=Filter)
@receiver(post_save, sender=AHU)
@receiver(post_save, sender=Plant)
@receiver(post_save, sender=User)
def audit_model_changes(sender, instance, created, **kwargs):
    """
    After a model is saved, log whether it was a creation or an update.
    """
    user, _, _ = get_request_details()
    if not user: return

    old_values, new_values = get_changed_data(instance)

    if created:
        log_audit_event(user, 'CREATE', instance, new_values=new_values)
    else:
        # Find what actually changed to avoid logging saves with no data changes
        changed_fields = {k: v for k, v in new_values.items() if str(v) != str(old_values.get(k))}
        if changed_fields:
            log_audit_event(user, 'UPDATE', instance, old_values=old_values, new_values=new_values)
    
    if hasattr(instance, '_old_instance'):
        del instance._old_instance


@receiver(post_delete, sender=Filter)
@receiver(post_delete, sender=AHU)
@receiver(post_delete, sender=Plant)
@receiver(post_delete, sender=User)
def audit_model_deletions(sender, instance, **kwargs):
    """
    Receiver for post_delete signal on our audited models.
    """
    user, _, _ = get_request_details()
    if not user: return
    
    old_values, _ = get_changed_data(instance)
    log_audit_event(user, 'DELETE', instance, old_values=old_values)


# --- Signal Receivers for Auth Auditing ---

@receiver(user_logged_in)
def audit_user_login(sender, request, user, **kwargs):
    """Receiver for user_logged_in signal."""
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    AuditLog.objects.create(
        user=user,
        action='USER_LOGIN',
        ip_address=ip,
        user_agent=user_agent,
        new_values={'message': f'User {user.username} logged in successfully.'}
    )

@receiver(user_logged_out)
def audit_user_logout(sender, request, user, **kwargs):
    """Receiver for user_logged_out signal."""
    if not user: return
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    AuditLog.objects.create(
        user=user,
        action='USER_LOGOUT',
        ip_address=ip,
        user_agent=user_agent,
        new_values={'message': f'User {user.username} logged out.'}
    )