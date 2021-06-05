from django.contrib import admin

# Register your models here.
from .models import Ad, Fav

admin.site.register(Ad)
admin.site.register(Fav)
