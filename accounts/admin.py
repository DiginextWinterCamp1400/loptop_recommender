from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import NewUserCreationForm, NewUserChangeForm
from .models import NewUser

class NewUserAdmin(UserAdmin):
    add_form = NewUserCreationForm
    form = NewUserChangeForm
    model = NewUser
    list_display = ['email', 'username',]

admin.site.register(NewUser, NewUserAdmin)