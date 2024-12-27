# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'  # Define the template name here
    success_url = reverse_lazy('login')  # Redirect to the login page after successful signup
