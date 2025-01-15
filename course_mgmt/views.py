from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm  # You will need to create a form for Course

# Create Course (Create Operation)
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new course
            return redirect('course_list')  # Redirect to course listing page
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

# List Courses (Read Operation)
def course_list(request):
    courses = Course.objects.all()  # Fetch all courses
    return render(request, 'course_list.html', {'courses': courses})

# View Course Detail (Read Operation)
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)  # Fetch course by ID
    return render(request, 'course_detail.html', {'course': course})

# Update Course (Update Operation)
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()  # Save the updated course
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'update_course.html', {'form': form, 'course': course})

# Delete Course (Delete Operation)
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        course.delete()  # Delete the course
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})
