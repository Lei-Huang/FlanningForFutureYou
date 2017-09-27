from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet, UserGroupViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'usergroups', UserGroupViewSet)


urlpatterns = router.urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)