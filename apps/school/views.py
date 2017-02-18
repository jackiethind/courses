from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Course


def index(request):
    context = {
        'courses' : Course.objects.all(),
    }

    return render(request,'school/index.html', context)
def process(request):
    if request.method == "POST":
        Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
        #insert into Course (name, course, created_at, updated_at) values (name, course, now(),now() )
        messages.add_message(request, messages.INFO, 'You added a new course!')
        print "Got Post Info"
        return redirect ('/')

def delete(request, id):
    print id
    if request.method == "POST":
        Course.objects.filter(id=id).delete()

    return redirect('/')

def complete_delete(request, id):
    if request.method == "POST":
        Course.objects.filter(id=id).delete()
    return redirect('/')
# Create your views here.
