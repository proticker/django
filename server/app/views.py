from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

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

# def maxNum(request): 
#     c = int(request.GET['num1'])
#     d = int(request.GET['num2'])
#     if(c < d): 
#         return HttpResponse(d)
#     else: 
#         return HttpResponse(c)
    
def number(request):
    return  render(request, 'evenodd.html')
def evenodd(request):
    x = int(request.GET['num'])
    if(x%2 == 0):
        return HttpResponse("num is even")
    else:
        return HttpResponse("num is odd")
    
     











        
