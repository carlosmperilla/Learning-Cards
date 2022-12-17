from django.urls import include, path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views


router = routers.DefaultRouter()
router.register(r'kits', views.KitViewSet)
router.register(r'cards', views.CardViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Learning Cards' API v1",
      default_version='v1',
      description="API v1, handle kits and cards.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="carlosperillaprogramacion@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]