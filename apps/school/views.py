from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Course, Description, Comment


def index(request):
    context = {
        'courses' : Course.objects.all(),
    }

    return render(request,'school/index.html', context)
def process(request):
    if request.method == "POST":
        if request.POST['submit']== 'Add':
            course=Course.objects.create(course_name=request.POST['name'])
            #insert into Course (name, course, created_at, updated_at) values (name, course, now(),now() )
            Description.objects.create(course=course, description=request.POST['description'])
            messages.add_message(request, messages.INFO, 'You added a new course!')
            print "Got Post Info" # DEBUG
            return redirect ('/')

def delete(request, id):
    print "Got Delete Request"
    if request.method == "POST":
        if request.POST['submit'] == 'Delete':
            Course.objects.filter(id=id).delete()
            return redirect('/')
        elif request.POST['submit'] == 'No':
            return redirect('/')
    else:
        course = Course.objects.get(id=id)
        context = {'course' : course}
        return render(request, 'school/delete.html', context)


def comments(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'comment': Comment.objects.filter(course=id),
    }
    print "Got Comment"
    if request.method == "POST":
        if request.POST['submit'] == 'Submit':
            comment=Comment.objects.create(comment=request.POST['comment'], course=Course.objects.get(id=id))
            messages.add_message(request, messages.INFO, 'You added a new comment!')
            id=id
            course = Course.objects.get(id=id)
            comment = Comment.objects.all()
            print comment
            context = {'course' : course,
                       'comments': comment}
            return render(request, 'school/comments.html', context)
        elif request.POST['submit'] == 'Back':
            return redirect('/')
    else:
        course = Course.objects.get(id=id)
        comment = Comment.objects.all()
        print comment
        context = {'course' : course,
                   'comments': comment}
        return render(request, 'school/comments.html', context)
# def comments_process(request,id):
#     print id
#
#     return redirect('/comments/{}'.format(id))
