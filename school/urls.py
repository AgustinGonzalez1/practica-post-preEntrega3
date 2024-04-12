from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="Student"),
  path("delete-student/<int:id>", views.delete_student, name="delete-student"),
  path("update-student/<int:id>", views.update_student, name="update-student"),
  path("teachers", views.teachers, name="Teachers"),
  path("teachers/delete-teacher/<int:id>", views.delete_teacher, name="delete-teacher"),
  path("teachers/update-teacher/<int:id>", views.update_teacher, name="update-teacher"),
  path("courses", views.courses, name="Courses"),
  path("courses/delete-course/<int:id>", views.delete_course, name="delete-course"),
  path("courses/update-course/<int:id>", views.update_course, name="update-course"),
  path("login", views.login_request, name="login"),
  path("inicio", views.inicio, name="inicio"),
  path("register", views.register, name="register"),
  path("logout", views.logout_request, name="logout"),
]
