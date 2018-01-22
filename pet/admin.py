from django.contrib import admin

from pet.models import Pet, MngLog


# Register your models here.

class MngLogPage(admin.ModelAdmin):
    list_display = ('id', 'pet', 'user', 'type', 'created_date')

class Petpage(admin.ModelAdmin):
    list_display = ('id', 'owner', 'nickname', 'created_date')


admin.site.register(Pet, Petpage)
admin.site.register(MngLog, MngLogPage)
