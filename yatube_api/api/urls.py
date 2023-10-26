from django.urls import include, path
from rest_framework import routers

from api.views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls))
]
