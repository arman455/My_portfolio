from django.shortcuts import render

# Create your views here.
def leisure_func(request):
    return render(request, "leisure/leisure.html")