# pharma_tracker/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from filters.views import PlantViewSet, AHUViewSet, FilterTypeViewSet, FilterViewSet
from cleaning.views import CleaningRecordViewSet, AuditLogViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'plants', PlantViewSet)
router.register(r'ahus', AHUViewSet)
router.register(r'filter-types', FilterTypeViewSet)
router.register(r'filters', FilterViewSet)
router.register(r'cleaning-records', CleaningRecordViewSet)
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]