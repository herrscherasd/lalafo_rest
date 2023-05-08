from rest_framework.routers import DefaultRouter

from apps.users.views import UsersAPIViewSet

router = DefaultRouter()
router.register( 'users', UsersAPIViewSet, "api_users")
urlpatterns = router.urls