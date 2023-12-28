from rest_framework.routers import SimpleRouter

from .views import FolderViewSet

router = SimpleRouter()
router.register('folders', FolderViewSet,
                basename='folders')

urlpatterns = router.urls
