from django.urls import path
from userapp.apis import GetUserView, AddUserView, UserLoginView, UserLogoutView, UserGetView, \
    GetAllProfilesAPI, GetUserProfileAPI, GetOwnUserProfileAPI, \
    GenerateUserLoginOTPAPI, UserValidateOTPAPI

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('otp-login/', GenerateUserLoginOTPAPI.as_view(), name='user_login_otp'),
    path('otp-validate/', UserValidateOTPAPI.as_view(), name='user_validate_otp'),
    path('logout/', UserLogoutView.as_view(), name='User_logout'),
    path('all/', GetUserView.as_view(), name='all_users'),
    path('add/', AddUserView.as_view(), name='add_user'),
    path('details/<slug:slug>', UserGetView.as_view(), name='get_user'),
    path('profile/all', GetAllProfilesAPI.as_view(), name='all_user_profiles'),
    path('profile/edit', GetOwnUserProfileAPI.as_view(), name='own_user_profile'),
    path('profile/<slug:slug>', GetUserProfileAPI.as_view(), name='get_user_profile'),
]
