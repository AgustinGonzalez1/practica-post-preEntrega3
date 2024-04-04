from django.shortcuts import render, redirect
from .models import Course, Student, Teacher
from school.forms import StudentForm, TeacherForm, CourseForm


# Create your views here.

def home(request):
  students = Student.objects.all()
  
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      student = Student(name=data['name'], course=data['course'], commission=data['commission'])
      student.save()
      return render(request, 'home.html', {'message': 'Alumno creado exitosamente', 'students': students})
  

  
  return render(request, 'home.html', {'students': students})

def courses(request):
  courses = Course.objects.all()
  
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      course = Course(name=data['name'], teacher=data['teacher'])
      course.save()
      return render(request, 'courses.html', {'message': 'Curso creado exitosamente', 'courses': courses})
  
  return render(request, 'courses.html', {'courses': courses})

def teachers(request):
  
  if request.method == 'POST':
    form = TeacherForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      teacher = Teacher(name=data['name'], course_name=data['course_name'])
      teacher.save()
      return render(request, 'teachers.html', {'message': 'Profesor creado exitosamente', 'teachers': teachers})
  
  name = request.GET.get("name")
  
  if name:
    teacher_filter = Teacher.objects.filter(name__icontains = request.GET["name"])
    return render(request, 'teachers.html', {'teacher_filter': teacher_filter})
  else:
    return render(request, 'teachers.html')

def delete_student(request, id):
  student = Student.objects.get(id=id)
  student.delete()
  
  return redirect('/')

def update_student(request, id):
  student = Student.objects.get(id=id)
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      student.name = data['name']
      student.course = data['course']
      student.commission = data['commission']
      student.save()
      return redirect('/')
  
  return render(request, 'updateStudent.html')