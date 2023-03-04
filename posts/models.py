from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE, default=None, null=True)
    category = models.CharField(max_length=50,
    choices=(
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Career', 'Career'),
        ('Database', 'Database'),
        ('Frameworks', 'Frameworks'),
        ('Github', 'Github'),
        ('Hackathons', 'Hackathons'),
        ('Languages', 'Languages'),

    ))
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now=True)



    def __str__(self):
        return self.heading
    

class Profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.TextField()
    lastname = models.TextField()
    email = models.EmailField(max_length=254)
    blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)


    def __str__(self):
        return self.username


