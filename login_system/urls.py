from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('success1/',views.success1,name='success1'),
]
