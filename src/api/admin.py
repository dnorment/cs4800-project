# Register your models here.
from django.contrib import admin
from .models import Hero
from .models import Bot


admin.site.register(Bot)
admin.site.register(Hero)
