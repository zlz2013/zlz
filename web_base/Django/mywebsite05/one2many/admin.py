from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Publisher)
admin.site.register(models.Book2)