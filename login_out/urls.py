from django.urls import path

from login_out import views

urlpatterns = [
    path('login',views.login,name= 'login'),
    path('logout',views.logout, name = 'logout')
]