# import requests
import account.views
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from account.forms import LoginEmailForm

from .forms import RegistrationForm


# Create your views here.
class HomePageView(TemplateView):
    """
    Home page view
    """
    template_name = "home.html"


class LoginView(account.views.LoginView):
    """
    Login view. User can login with email and password
    """
    form_class = LoginEmailForm


class RegistrationView(CreateView):
    """
    Create a new customer account if not registered already
    """
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = "account/registration.html"

