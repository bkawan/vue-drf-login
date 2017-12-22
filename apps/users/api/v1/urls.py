from rest_framework.routers import DefaultRouter

from .views import UserViewSet

app_name = 'users_api_v1'
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns = router.urls
