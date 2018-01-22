from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from pet.models import Pet

def home(request):
    # body = HttpResponse("My Pets!!")
    if request.user.is_authenticated():
        user = request.user
        mypet = Pet.objects.get(owner=user)
        return redirect('pet:pet_detail', mypet.id)
    else:
        # return render(request, 'home.html')
        return redirect('pet:pet_list')


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'
