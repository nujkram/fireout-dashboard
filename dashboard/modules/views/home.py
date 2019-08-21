import pyrebase
from django.conf import settings
from django.shortcuts import render
from django.views import View
from firebasedata import LiveData

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

auth = firebase.auth()
db = firebase.database()

live = LiveData(firebase, '/my_data')

data = live.get_data()
all_data = data.get()
sub_data = data.get('my/sub/path')

def my_handler(data):
  print(data)


class DashboardHomeView(View):
  def get(self, request, *args, **kwargs):
    all_firebase_users = db.child('Users').get()
    all_users = {}
    for user in all_firebase_users.each():
      all_users[user.key()] = user.val()

    notification = live.signal('/some/key').connect(my_handler)

    context = {
      'page_title': 'FireOut: Home',
      'location': 'home',
      'all_users': all_users,
      'notification': notification,
    }

    return render(request, 'dashboard/home.html', context)
