from django.urls import path
from frontend.views import index, IdeaDetailView

urlpatterns = [
    path('', index),
    path('edit/<int:pk>', IdeaDetailView.as_view()),
    path('delete/<int:pk>', IdeaDetailView.as_view()),
]

