from distutils.command.upload import upload
from os import link
import profile
from tabnanny import verbose
from turtle import update
from django.db import models

# Create your models here.

class Home(models.Model):
    name = models.CharField(max_length=20)
    greeting_1 = models.CharField(max_length=5)
    greeting_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    #save time when modified
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

 # ABOUT SECTION

class About(models.Model):
        heading = models.CharField(max_length=50)
        career = models.CharField(max_length=20)
        description = models.TextField(blank=False)
        profile_img = models.ImageField(upload_to='profile/')

        updated = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.career    

class Profile(models.Model):
        about = models.ForeignKey('About', on_delete=models.CASCADE)
        social_name = models.CharField(max_length=10)
        link = models.URLField(max_length=200)




#skill Section

class Category(models.Model):
    name = models.CharField(max_length=20)

    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


class Skills(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)



#portfolio Section

class Portfolio(models.Model):
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return f'portfolio {self.id}'
        
    