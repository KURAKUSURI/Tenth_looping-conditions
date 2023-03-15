from django.shortcuts import render

# Create your views here.

def loop(request):
    s={'name': 'SURI'}
    return render(request,'loop.html',s)
