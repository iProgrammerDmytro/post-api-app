from django.urls import path

from rest_framework import routers

from .views import PostsViewSet

# если начальный путь был api переходим на эти urls
router = routers.DefaultRouter()
router.register('posts', PostsViewSet)

urlpatterns = router.urls