from rest_framework.routers import DefaultRouter

from apps.categories.views import CategoryAPIViewSet

router = DefaultRouter()
router.register('category', CategoryAPIViewSet, 'api_category')

urlpatterns = router.urls