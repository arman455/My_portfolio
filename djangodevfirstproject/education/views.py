from django.shortcuts import render

# Create your views here.
def education_func(request):
    return render(request, "education/education.html")