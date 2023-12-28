from rest_framework.routers import SimpleRouter

from .views import ProfileViewSet

app_name = "profiles"

router = SimpleRouter()
router.register("profiles", ProfileViewSet, basename="profiles")

urlpatterns = router.urls


