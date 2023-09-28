from django.shortcuts import render

# Create your views here.
def hobbies_func(request):
    return render(request, "hobbies/hobbies.html")