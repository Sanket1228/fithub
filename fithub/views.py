from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        dob = request.POST.get('dob','')
        gender = request.POST.get('gender','')
        number = request.POST.get('number','')
        level = request.POST.get('level','')
        height = request.POST.get('height','')
        weight = request.POST.get('weight','')
        age = request.POST.get('age','')
        bmi = request.POST.get('bmi','')
        fat = request.POST.get('fat','')


    return render(request,'registration.html')

def bmiCalculate(request):
    if request.method == "POST":
        data = json.loads(request.POST['params'])
        height = int(data['height'])
        weight = int(data['weight'])
        bmi = (weight / height * height) * 10000
        response = json.dumps({"bmiValue":bmi},default=int)
        return HttpResponse(response)
