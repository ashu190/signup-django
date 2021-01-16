from django.contrib import admin
from signupApp.models import Signup

# Register your models here.
@admin.register(Signup)
class signupAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone", "password1", "password2")

