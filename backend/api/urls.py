from rest_framework import routers
from backend.api.views import IdeaViewSet

router = routers.DefaultRouter()
router.register('ideas', IdeaViewSet)

urlpatterns = router.urls

