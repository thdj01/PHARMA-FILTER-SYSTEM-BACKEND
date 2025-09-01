# cleaning/middleware.py

import threading

_request_storage = threading.local()

class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _request_storage.request = request
        response = self.get_response(request)
        return response

def get_current_request():
    """Returns the current request object."""
    return getattr(_request_storage, 'request', None)

def get_request_details():
    """Helper function to extract user, IP, and user agent from the current request."""
    request = get_current_request()
    if not request:
        return None, None, None

    user = request.user if request.user.is_authenticated else None
    
    # Get IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        
    user_agent = request.META.get('HTTP_USER_AGENT')
    
    return user, ip, user_agent