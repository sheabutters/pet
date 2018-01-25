from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
import pytz

from pet.models import Pet, MngLog
from pet.forms import PetForm

# Create your views here.


def pet_list(request):
    lst = Pet.objects.all()
    return render(request, 'pet/pet_list.html', {'pet_list': lst})


def pet_detail(request, pet_id):
    if pet_id:
        pet = get_object_or_404(Pet, pk=pet_id)
        log_list = pet.mnglog_set.all().order_by('-created_date')[:10]
        return render(request, 'pet/pet_detail.html', {'pet': pet, 'log_list': log_list})
    else:
        return redirect('pet:pet_list')


# @login_required
# def pet_new(request):
#     if request.method == 'POST':
#         form = PetForm(request.POST)
#         if form.is_valid():
#             pet = Pet()
#             pet.nickname = form.cleaned_data['nickname']
#             pet.owner = request.user
#             pet.save()
#
#             return redirect(pet)
#     else:
#         form = PetForm()
#     return render(request, 'pet/pet_edit.html', {'form': form})


@login_required
def mng_new(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    if request.method == 'POST':
        mng = MngLog()
        mng.type = request.POST['type']
        mng.save()

        return redirect(pet)


def pet_mng(request):
    pk = request.POST.get('pk', None)
    pet = get_object_or_404(Pet, pk=pk)
    type = request.POST.get('type', None)
    pet.mnglog_set.create(pet=pet, user=request.user, type=type)

    return HttpResponse(json.dumps(pet.mng_log), content_type="application/json")


def pet_mng_log(request):
    pk = request.GET.get('pk', None)
    pet = get_object_or_404(Pet, pk=pk)
    log_list = pet.mnglog_set.all().order_by('-created_date')[:1]
    data = []
    timezone = pytz.timezone('Asia/Seoul')
    for log in log_list:
        now = log.created_date.astimezone(tz=timezone)
        obj = {}
        obj['year'] = now.year
        obj['month'] = now.month
        obj['day'] = now.day
        obj['hour'] = now.hour
        obj['minute'] = now.minute
        obj['user'] = log.user.username
        obj['type'] = log.type
        data.append(obj)

    return HttpResponse(json.dumps(data), content_type="application/json")

def pet_name(request):
    pk = request.GET.get('pk', None)
    pet = get_object_or_404(Pet, pk=pk)
    user = request.user
    owner = pet.owner
    data = {}
    if (user == owner):
        name = request.GET.get('petname', None)
        pet.nickname = name
        pet.save()
        data['state'] = True
    else:
        data['state'] = False
        data['message'] = "변경권한이 없습니다."
        data['petname'] = pet.nickname
    return JsonResponse(data)
