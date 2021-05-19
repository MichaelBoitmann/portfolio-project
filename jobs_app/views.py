from django.shortcuts import render

# Create your views here.


def boitmann(request):
    return render(request, 'jobs/home.html')
