from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import Job
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def jobs(request):
    job = Job.objects.order_by('-id')
    return render(request, 'jobs.html', {'job': job})


def jobdetail(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'jobdetail.html', {'job': job})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        try:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful')
            return redirect('login')
        except:
            messages.error(request, 'Username already exists')
            return redirect('register')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('jobs')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('jobs')


@login_required(login_url='login')
def postjob(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company')
        location = request.POST.get('location')
        position = request.POST.get('job_field')
        image = request.FILES.get('image')
        desc = request.POST.get('job_description')
        apply_url = request.POST.get('apply_url')
        desc = strip_tags(desc)


        job = Job(
            job_title=job_title,
            company_name=company_name,
            location=location,
            position=position,
            image=image,
            desc=desc,
            apply_url=apply_url
        )
        job.save()

        return redirect('/')

    return render(request, 'postjob.html')

def updatejob(request):
    return render(request, 'updatejob.html')
