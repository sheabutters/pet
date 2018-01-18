from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def home(request):
    # body = HttpResponse("My Pets!!")
    if request.user.is_authenticated():
        return redirect('pet:pet_detail', 1)
    else:
        return render(request, 'home.html')

