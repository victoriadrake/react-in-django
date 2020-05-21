from django.shortcuts import render
from django.views.generic import DetailView

from backend.models import Idea

def index(request):
    return render(request, 'frontend/index.html')


class IdeaDetailView(DetailView):
    model = Idea
    template_name = 'frontend/index.html'

