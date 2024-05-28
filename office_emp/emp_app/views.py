from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee,Role,Department
from emp_app.forms import SignUpForm
from emp_app.forms import LoginForm
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        salary= int(request.POST['salary'])
        bonus= int(request.POST['bonus'])
        phone= int(request.POST['phone'])
        dept= int(request.POST['dept'])
        role= int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,phone=phone,bonus=bonus,dept=dept,role=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("employee added succussfully")
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("sorry employee nod add")

def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed succesufully")
        except:
            return HttpResponse("please enter a valid emp_id")

    emps=Employee.objects.all()
    context={
        'emps':emps
    }

    return render(request,'remove_emp.html',context)

def filter_emp(request):
    return render(request,'filter_emp.html')

def about_us(request):
    return render(request,"about_us.html")


def contact(request):
    return render(request,"contact.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirect to home page after successful login
            else:
                error_message = "Invalid username or password."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
            # Redirect or do something upon successful form submission
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
