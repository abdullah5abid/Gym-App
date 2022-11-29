from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name="Index"),
    path('api/sessions/', views.SessionsAPI, name="SessionsAPI"),
    path('api/sessions/add/', views.AddSessionAPI, name="AddSessionAPI"),
    path('api/sessions/<int:id>/', views.SessionDetailsAPI, name="SessionDetailsAPI"),
    path('api/sessions/edit/<int:id>/', views.EditSessionAPI, name="EditSessionAPI"),
    path('api/sessions/delete/<int:id>/', views.DeleteSessionAPI, name="DeleteSessionAPI"),
]
