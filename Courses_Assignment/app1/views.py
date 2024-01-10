from django.shortcuts import render,redirect
from .models import Courses
from .forms import CoursesForms
from django.contrib import messages

# Create your views here.


def home(request):
    context = {
        'form': CoursesForms(), 
        'courses': Courses.objects.all()
    }
    if request.method == 'POST':
        errors = Courses.objects.validate(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, 'add_course.html', context)
        else:
            form = CoursesForms(request.POST)
            if form.is_valid():
                form.save()
                return redirect('app1:home')

    return render(request, 'add_course.html', context)



def remove(request, pk):
    course_to_delete = Courses.objects.get(id=pk)
    context={
        'course': course_to_delete
    }
    return render(request,'delete_course.html', context)


def destroy(request, pk):
    Courses.objects.get(id=pk).delete()
    return redirect('app1:home')

