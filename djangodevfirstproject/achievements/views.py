from django.shortcuts import render

# Create your views here.
def achievements_func(request):
    return render(request, "achievements/achievements.html")