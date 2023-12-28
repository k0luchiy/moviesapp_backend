from rest_framework.routers import SimpleRouter

from .views import MovieViewSet, MovieInteractionViewSet

app_name = "movies"

router = SimpleRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("movie-interaction", MovieInteractionViewSet, basename="movie-interaction")

urlpatterns = router.urls