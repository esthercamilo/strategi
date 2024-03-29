import os

from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation - Marvel heroes management",
        default_version='v1',
        contact=openapi.Contact(email="esthercamilo@gmail.com"),
    ),
    url=os.environ.get('URL', 'http://127.0.0.1:8000/'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('app.urls')),
    path('api-auth/', include('rest_framework.urls'))
]