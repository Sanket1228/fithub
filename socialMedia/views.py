from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration


def index(request):
    return render(request, 'socialMedia/index.html')


def registration(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        number = request.POST.get('number', '')
        level = request.POST.get('level', '')
        height = request.POST.get('height', '')
        weight = request.POST.get('weight', '')
        age = request.POST.get('age', '')
        bmi = request.POST.get('bmi', '')
        fat = request.POST.get('fat', '')
        register = Registration(name=name,email=email,DOB=dob,gender=gender,
        mobile_number=number,fitness_level=level,height=height,weight=weight,age=age,bmi=bmi,fat_per=fat)
        register.save()

    return render(request, 'socialMedia/registration.html')
