from . import views
from django.urls import path


urlpatterns = [
    path('users/<str:token>/', views.UserDetailsView.as_view(), name='users_view'),
    path('heroes/', views.HeroesView.as_view(), name='heores_view')
]