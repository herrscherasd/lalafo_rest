from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, FavoritePosAPIViewSet


router = DefaultRouter()
router.register('posts', PostAPIViewSet, "api_posts")
router.register('favourites', FavoritePosAPIViewSet, 'api_favorite_posts')

urlpatterns = router.urls