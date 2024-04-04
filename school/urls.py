from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="Student"),
  path("delete-student/<int:id>", views.delete_student, name="delete-student"),
  path("update-student/<int:id>", views.update_student, name="update-student"),
  path("teachers", views.teachers, name="Teachers"),
  path("courses", views.courses, name="Courses"),
]
