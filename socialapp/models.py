from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your models here.
class UserRegistration_model(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)

   
    def __str__(self):
        return f"{self.name} {self.email} {self.password}"
    


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Post"

