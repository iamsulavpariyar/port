from turtle import home
from django.contrib import admin
from sulav.models import Home, About, Profile, Category, Skills, Portfolio

# Register your models here.

#home
admin.site.register(Home)


#about
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

#skill

class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)    
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SkillsInline,
    ]


#portfolio
admin.site.register(Portfolio)