import pyrebase
from django.conf import settings
from django.shortcuts import render
from django.views import View

from helpers.analytics import count_user_per_location

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

auth = firebase.auth()
db = firebase.database()


class DashboardHomeView(View):
  def get(self, request, *args, **kwargs):
    users_by_province = count_user_per_location()
    firebase_users = db.child('Users').get()
    users = {}

    for user in firebase_users.each():
      users[user.key()] = user.val()

    context = {
      'page_title': 'FireOut: Home',
      'location': 'home',
      'users': users,
      'users_by_province': users_by_province,
    }

    return render(request, 'dashboard/home.html', context)
