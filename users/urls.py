from rest_framework.routers import SimpleRouter
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CustomUserViewSet

app_name = "users"

router = SimpleRouter()
router.register("users", CustomUserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    # path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("login/", LoginView.as_view(), name="login"),
    # path("logout/", LogoutView.as_view(), name="logout"),
]
