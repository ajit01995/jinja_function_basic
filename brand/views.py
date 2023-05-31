from django.shortcuts import render

# Create your views here.
def uspa(request):
    d={'name' : 'ajit','surname': 'kumar'}
    return render(request,'uspa.html',d)
