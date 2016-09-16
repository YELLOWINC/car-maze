from django.shortcuts import render
from cars.models import UserProfile


def home(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'home.html', {'user_profile': user_profile})
    return render(request, 'home.html')