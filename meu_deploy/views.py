from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse



def home(request):
    # return redirect(reverse('dashboardapp:home'))
    return render(request, 'inicio.html')