from django.contrib import admin
from .models import MissingPerson, Gender, Race
# Register your models here.

admin.site.register(MissingPerson)
admin.site.register(Gender)
admin.site.register(Race)