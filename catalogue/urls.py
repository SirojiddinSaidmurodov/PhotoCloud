from django.urls import path

from catalogue import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup', views.signup, name='signup'),
    path('account', views.account, name='account'),
    path('upload', views.upload, name='upload')
]
