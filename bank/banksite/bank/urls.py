from django.urls import path
from . import views


urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('new_page', views.new_page, name='new_page'),
    path('form_page/', views.form_page, name='form_page'),
    path('form_submit/', views.application_submit, name='application_submit'),
    path('logout', views.logout, name='logout'),

]
