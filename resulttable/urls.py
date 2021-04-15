from django.conf.urls import url, include
from .views import PostTeamViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("admin-post-results", PostTeamViewSet, basename="posts")

urlpatterns = [
    url('', include(router.urls)),
]
