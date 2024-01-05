from app.views import update_marvel_heroes_endpoint
from . import views
from django.urls import path


urlpatterns = [
    path('users/get/<int:user_id>', views.UsersView.as_view({'get': 'get'}), name='users_get_view'),
    path('users/list/', views.UsersView.as_view({'get': 'list'}), name='users_list_view'),
    path('users/create/', views.UsersView.as_view({'post': 'create_new_user'}), name='users_create_view'),
    path('users/auth/', views.auth, name='users_auth_view'),

    path('heroes/get/<int:hero_id>/', views.HeroesView.as_view({'get': 'get'}), name='heroes_get_view'),
    path('heroes/filter/<int:hero_id>/', views.HeroesView.as_view({'get': 'filter'}), name='heroes_filter_view'),
    path('heroes/delete/<int:hero_id>/', views.HeroesView.as_view({'delete': 'delete'}), name='heroes_delete_view'),
    path('heroes/list/', views.HeroesView.as_view({'get': 'list'}), name='heroes_list_view'),
    path('heroes/upsert/', views.HeroesView.as_view({'post': 'post'}), name='heroes_upsert_view'),
    path('heroes/populate/', update_marvel_heroes_endpoint, name='populate_heroes_view'),

    path('groups/get/<int:group_id>/', views.GroupsView.as_view({'get': 'get'}), name='groups_get_view'),
    path('groups/delete/<int:group_id>/', views.GroupsView.as_view({'delete': 'delete'}), name='groups_delete_view'),
    path('groups/list/', views.GroupsView.as_view({'get': 'list'}), name='groups_list_view'),
    path('groups/upsert/', views.GroupsView.as_view({'post': 'post'}), name='groups_upsert_view')

]

