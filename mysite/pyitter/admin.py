from django.contrib import admin

# Register your models here.

from .models import User,Tweet

admin.site.register(User)
admin.site.register(Tweet)