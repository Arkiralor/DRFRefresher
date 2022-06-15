from django.urls import path
from userapp.apis import GetUserView, AddUserView, UserLoginView, UserLogoutView, \
    UserGetView, GetAllProfilesAPI, UserLoginOTPAPI, UserValidateOTPAPI

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('otp-login/', UserLoginOTPAPI.as_view(), name='user_login_otp'),
    path('otp-validate/', UserValidateOTPAPI.as_view(), name='user_validate_otp'),
    path('logout/', UserLogoutView.as_view(), name='User_logout'),
    path('all/', GetUserView.as_view(), name='all_users'),
    path('add/', AddUserView.as_view(), name='add_user'),
    path('details/<str:slug>', UserGetView.as_view(), name='get_user'),
    path('profile/all', GetAllProfilesAPI.as_view(), name='all_user_profiles'),
]
