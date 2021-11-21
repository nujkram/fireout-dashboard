import pyrebase
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.contrib import messages

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

auth = firebase.auth()

class LoginView(View):
  def get(self, request, *args, **kwargs):
    context = {
      'page_title': 'FireOut Dashboard',
    }

    return render(request, 'account/login.html', context)

  def post(self, request, *args, **kwargs):
    db = firebase.database()
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    try:
      user = auth.sign_in_with_email_and_password(email=email, password=password)
      return HttpResponseRedirect(reverse('dashboard_home_view'))
    except:
      messages.error(request, 'Invalid username or password', extra_tags='danger')

    context = {
      'page_title': 'FireOut Dashboard',
      'location': 'login',
    }

    return render(request, 'account/login.html', context)