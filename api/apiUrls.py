from django.urls import URLPattern, path
from rest_framework import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls))
] 