from django.urls import path
from userapp.apis import GetUserView, AddUserView, UserLoginView, UserLogoutView, SetSuperView, \
    SetStaffView, UserGetView, MakeModeratorView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='User_logout'),
    path('all/', GetUserView.as_view(), name='all_users'),
    path('add/', AddUserView.as_view(), name='add_user'),
    path('details/<str:slug>', UserGetView.as_view(), name='get_user'),
    path('make_super/<str:slug>', SetSuperView.as_view(), name='set_super'),
    path('make_staff/<str:slug>', SetStaffView.as_view(), name='set_staff'),
    path('make_moderator/<str:slug>', MakeModeratorView.as_view(), name='make_moderator'),
]