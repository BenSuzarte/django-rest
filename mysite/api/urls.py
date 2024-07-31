from django.urls import path
from . import views

urlpatterns = [
  path('task/', views.TaskPostListCreate.as_view(), name="tasks-view-create"),
  path('task/<int:pk>/', views.TaskPostRetrieveUpdateDestroy.as_view(), name="tasks-update")
]