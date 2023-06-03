from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def calculate(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    op=request.POST["op"]
    res=0
    data=""
    if op=="add":
        res=x+y
        data="The Sum is: "
    elif op=="sub":
        res=x-y
        data="The Sub is: "
    elif op=="mul":
        res=x*y
        data="The Mul is: "
    else:
        res=x/y
        data="The Division is: "
    return HttpResponse(data+str(res))


# Create your views here.
