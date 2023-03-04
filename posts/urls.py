from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginApp, name='login'),
    path('logout/', views.logoutApp, name='logout'),
    path('register/', views.register, name='register'),
    path('view_profile', views.viewProfile, name='profile'),
    path('frontend/', views.frontend, name='frontend'),
    path('backend/', views.backend, name='backend'),
    path('career/', views.career, name='career'),
    path('database/', views.database, name='database'),
    path('frameworks/', views.frameworks, name='frameworks'),
    path('github/', views.github, name='github'),
    path('hackathons/', views.hackathons, name='hackathons'),
    path('languages/', views.languages, name='languages'),
    path('add/', views.addData, name='data'),
    path('add/posted/', views.blogsPosted, name='blogsPosted'),
    path('<int:id>', views.singleBlog, name='singleBlog'),

]