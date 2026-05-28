from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('monitor/', views.monitor, name='monitor'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('api/datasets/', views.api_get_datasets, name='api_datasets'),
    path('api/system/', views.api_system_stats,name='api_system_stats'),
]