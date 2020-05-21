from rest_framework import viewsets
from backend.api.serializers import IdeaSerializer
from backend.models import Idea

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

