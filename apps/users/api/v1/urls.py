from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, SignupView

app_name = 'users_api_v1'
urlpatterns = [
    url(r'^signup/$', SignupView.as_view())
]
router = DefaultRouter()
router.register('users', UserViewSet)
urlpatterns += router.urls
