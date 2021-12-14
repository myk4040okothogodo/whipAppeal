from rest_framework.routers import DefaultRouter
from whippAPI.user.viewsets import UserViewSet
from whippAPI.auth.viewsets.login import LoginViewSet
from whippAPI.auth.viewsets.register import RegistrationViewSet 
from whippAPI.auth.viewsets.refresh import RefreshViewSet
from . import views


routes = DefaultRouter()

# AUTHENTICATION
routes.register(r'auth/login', LoginViewSet, basename='auth-login')
routes.register(r'auth/register', RegistrationViewSet, basename='auth-register')
routes.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

# USER
routes.register(r'user', UserViewSet, basename='user')

#ACCOUNT
routes.register(r'accounts', views.AccountViewSet, basename='user-accounts')
routes.register(r'accounts/<int:id>/details', views.AccountDetails, basename='account-details')

urlpatterns = [
    *routes.urls
]
