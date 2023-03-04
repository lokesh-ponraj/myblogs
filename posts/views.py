from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog, Profile
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.forms import ValidationError
from .decorators import unAuthenticated_user
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password

# Create your views here.


@unAuthenticated_user
def home(request):
    home_blogs = list(Blog.objects.all())
    return render(request, 'posts/home.html', {'home_blogs': home_blogs})


@login_required(login_url='login')
def frontend(request):
    frontend_blogs = list(Blog.objects.filter(category='Frontend'))
    return render(request, 'posts/frontend.html', {'frontend_blogs': frontend_blogs})


@login_required(login_url='login')
def backend(request):
    backend_blogs = list(Blog.objects.filter(category='Backend'))
    return render(request, 'posts/backend.html', {'backend_blogs': backend_blogs})


@login_required(login_url='login')
def database(request):
    database_blogs = list(Blog.objects.filter(category='Database'))
    return render(request, 'posts/database.html', {'database_blogs': database_blogs})


@login_required(login_url='login')
def frameworks(request):
    frameworks_blogs = list(Blog.objects.filter(category='Frameworks'))
    return render(request, 'posts/frameworks.html', {'frameworks_blogs': frameworks_blogs})


@login_required(login_url='login')
def career(request):
    career_blogs = list(Blog.objects.filter(category='Career'))
    return render(request, 'posts/career.html', {'career_blogs': career_blogs})


@login_required(login_url='login')
def github(request):
    github_blogs = list(Blog.objects.filter(category='Github'))
    return render(request, 'posts/github.html', {'github_blogs': github_blogs})


@login_required(login_url='login')
def hackathons(request):
    hackathons_blogs = list(Blog.objects.filter(category='Hackathons'))
    return render(request, 'posts/hackathons.html', {'hackathons': hackathons_blogs})


@login_required(login_url='login')
def languages(request):
    languages_blogs = list(Blog.objects.filter(category='Languages'))
    return render(request, 'posts/languages.html', {'languages_blogs': languages_blogs})


@unAuthenticated_user
def loginApp(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Invalid user credentials..!')
            return render(request, 'posts/login.html')

        else:
            login(request, user)
            return redirect('frontend')

    return render(request, 'posts/login.html')


@unAuthenticated_user
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpass = request.POST.get('confpass')

        if password == confpass:
            if User.objects.filter(username=username).exists():
                messages.info(
                    request, 'Username is taken. Try another one')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords doesn't match ")
            return redirect('register')
    else:
        return render(request, 'posts/register.html')


def viewProfile(request):
    return render(request, 'posts/view_profile.html')


@login_required(login_url='login')
def addData(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        content = request.POST.get('content')
        date = request.POST.get('date')

        blog = Blog(
            category = category,
            heading = heading,
        description = description,
            content = content,
            date = date,
            )
        blog.save()
        return redirect('posted/')
    return render(request, 'posts/data.html')


def blogsPosted(request):
    return render(request, 'posts/blog_posted.html')


@login_required(login_url='login')
def singleBlog(request, id):
    single_blog = get_object_or_404(Blog, pk= id)
    return render(request, 'posts/single_blog.html', {'single_blog':single_blog})


@login_required(login_url='login')
def logoutApp(request):
    logout(request)
    return redirect(loginApp)
