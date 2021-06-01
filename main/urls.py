from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('sprav/', views.sprav, name='sprav'),
    path('sprav/materials/', views.sprav_mat, name='sprav_mat'),
    path('sprav/respons_persons/', views.sprav_persons, name='sprav_persons'),
    path('sprav/org/', views.sprav_org, name='sprav_org'),
    path('mat_on_sklad/', views.mat_on_skald, name='mat_on_sklad'),
]
