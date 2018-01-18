from django.contrib import admin

from pet.models import Pet, MngLog


# Register your models here.

class MngLogPage(admin.ModelAdmin):
    list_display = ('id', 'pet', 'user', 'type', 'created_date')


admin.site.register(Pet)
admin.site.register(MngLog, MngLogPage)
