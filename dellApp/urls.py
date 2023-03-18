from django.urls import path
from .views import *

urlpatterns=[
    path('index/',index),
    path('signup',signup_page, name='signup_page'),
    path('',signin_page, name='signin_page'),
    path('forgot_page/',forgot_page, name='forgot_page'),
    path('profile_page/',profile_page, name='profile_page'),

    path('signup/',signup, name='signup'),
    path('signin/',signin, name='signin'),
    path('load_data/',load_data, name='load_data'),
    path('password_reset/',password_reset, name='password_reset'),
    path('logout/',logout, name='logout'),
    path('update_data/',update_data, name='update_data'),
    path('delete_account/',delete_account, name='delete_account'),
    # path('profile_data/',profile_data, name='profile_data'),
]