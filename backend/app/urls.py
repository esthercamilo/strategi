from . import views
from django.urls import path


urlpatterns = [
    path('users/<str:token>/', views.UserDetailsView.as_view(), name='users_view'),
    path('heroes/', views.HeroesView.as_view(), name='heores_view'),
    path('groups/get/<int:group_id>/', views.GroupsView.as_view({'get': 'get'}), name='groups_get_view'),
    path('groups/delete/<int:group_id>/', views.GroupsView.as_view({'delete': 'delete'}), name='groups_delete_view'),
    path('groups/list/', views.GroupsView.as_view({'get': 'list'}), name='groups_list_view'),
    path('groups/upsert/<int:group_id>/', views.GroupsView.as_view({'post': 'post'}), name='groups_upsert_view')
]

