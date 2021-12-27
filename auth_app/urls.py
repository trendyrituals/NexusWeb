from django.urls import path
from .views import login_view,sign_view_B2B,logout_,check,sign_view_B2C,sign_view_agent,sign_view_B2E
urlpatterns = [
    path('check/',check,name='logout_help_url'),
    path('logout/',logout_,name='logout_help_url'),
    path('login/', login_view, name='auth_login_url'),
    path('sign_up_B2B/', sign_view_B2B,name='auth_sign_up_url'),
    path('sign_up_B2C/', sign_view_B2C,name='auth_sign_up_url'),
    path('sign_up_B2E/', sign_view_B2E,name='auth_sign_up_url'),
    path('sign_up_agent/', sign_view_agent,name='auth_sign_up_url')
]
