# accounts/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import NewUserCreationForm

class SignUpView(CreateView):
    form_class = NewUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'