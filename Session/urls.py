from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('index/', views.Index, name='index'),
    path('signout/', views.signout, name='signout'),
    path('api/sessions/', views.SessionsAPI, name="SessionsAPI"),
    path('api/sessions/add/', views.AddSessionAPI, name="AddSessionAPI"),
    path('api/sessions/<int:id>/', views.SessionDetailsAPI, name="SessionDetailsAPI"),
    path('api/sessions/edit/<int:id>/', views.EditSessionAPI, name="EditSessionAPI"),
    path('api/sessions/delete/<int:id>/', views.DeleteSessionAPI, name="DeleteSessionAPI"),
    path('users_list/', views.users_list, name="users_list"),
]
