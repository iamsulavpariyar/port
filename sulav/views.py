from contextvars import Context
import profile
from turtle import home
from unicodedata import category
from django.shortcuts import render, HttpResponse
from .models import Home, About, Portfolio, Category, Skills, Profile

# Create your views here.
def index(request):
    #home
    home = Home.objects.latest('update')
    #about
    about = About.objects.latest('updated')
    profile = Profile.objects.filter(about=about)

    #skill
    categories = Category.objects.all()

    #portfolio
    portfolios = Portfolio.objects.all()

    context = {'home': home, 'about': about, 'profile': profile, 'categories': categories, 'portfolios': portfolios}

    return render(request, 'index.html', context)

 