from django.contrib import admin
from django.urls import path
from .views import by_rubric, index, BbCreateView

urlpatterns = [
    path("", index, name='index'),
    path("<int:rubric_id>/", by_rubric, name='by_rubric'),
    path("add/", BbCreateView.as_view(), name='add'),
]
