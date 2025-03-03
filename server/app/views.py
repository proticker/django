from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from app.models import userdata 
from app.models import Student

# Create your views here. with arguments

def test(request):
    return HttpResponse("this is my first")
def home(request):
    return HttpResponse("hello world")
def index(request):
    return render(request,'index.html')
def sample1(request):
    return render(request,'sample1.html')
def sample2(request):
    return render(request,'sample2.html')
def index2(request):
    return render(request,'index2.html')
def add(request):
    return render(request,'add.html')

def addcode(request):
    
    a1 = request.GET.get('a1')
    a2 = request.GET.get('a2')
    
    # Check if both a1 and a2 are provided
    if a1 is None or a2 is None:
        return JsonResponse({"error": "Both 'a1' and 'a2' are required."}, status=400)
    
    try:
        a = int(a1)
        b = int(a2)
        c = a + b
        return HttpResponse(str(c))
    except ValueError:
        return JsonResponse({"error": "Invalid input. Please provide valid integers for a1 and a2."}, status=400)    
    
def nums(request): 
    return render(request, 'maxnum.html')

def maxNum(request): 
    c = int(request.GET['num1'])
    d = int(request.GET['num2'])
    if(c < d): 
        return HttpResponse(d)
    else: 
        return HttpResponse(c)
    
def number(request):
    return  render(request, 'evenodd.html')
def evenodd(request):
    x = int(request.GET['num'])
    if(x%2 == 0):
        return HttpResponse("num is even")
    else:
        return HttpResponse("num is odd")
def signup(request):
    return render(request,'signup.html')
    
def sign(request):
    u = userdata()
    u.Name= request.GET['c1']
    u.Email= request.GET['c2']
    u.Contact=request.GET['c3']
    u.Gender= request.GET['gender']
    u.Password= request.GET['c5']
    u.save()
    return render(request,'signup.html')

def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        roll = request.POST.get("roll")
        sec = request.POST.get("sec")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        guardian_name = request.POST.get("guardian_name")
        country = request.POST.get("country")
        gender = request.POST.get("gender")

        # Create Student Entry
        student = Student.objects.create(
            name=name,
            roll=roll,
            sec=sec,
            address=address,
            contact=contact,
            email=email,
            guardian_name=guardian_name,
            country=country,
            gender=gender
        )

        return HttpResponse(f"Student {student.name} added successfully!", content_type="text/plain")

    return render(request, "add_student.html")
def login(request):
    return render(request,'login.html')
def log(request):
    a= request.GET['email']
    b= request.GET['password']
    if userdata.objects.filter(Email=a,Password=b):
        return render(request,'signup.html')
    else:
        return render(request,'login.html')
    
def logout(request):
    return render(request,'logout.html')

def show(request):
    a=userdata.objects.all()
    return render(request,'show.html',{'x':a})#json format

def dele(request,id):
    d=userdata.objects.get(id=id)
    d.delete()
    return redirect('../show')

def edit(request,id):
    e=userdata.objects.get(id=id)
    return render(request,'edit.html',{'x':e})#jason format
def encode(request,id):
    d = userdata()
    d.Name= request.GET['c1']
    d.Email= request.GET['c2']
    d.Contact=request.GET['c3']
    d.Gender= request.GET['gender']
    d.Password= request.GET['c5']
    d.save()
    return render(request,'show.html')