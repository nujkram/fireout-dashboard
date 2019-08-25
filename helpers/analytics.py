import pyrebase
from django.conf import settings

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

auth = firebase.auth()
db = firebase.database()

def count_user_per_location() -> dict:
  """
  Count the number of users per location
  :return:
  """
  firebase_users = db.child('Users').get()
  users = {}
  provinces = {}
  for user in firebase_users.each():
    users[user.key()] = user.val()

  for key, data in users.items():
    if data['UserProvince'] not in provinces:
      provinces[data['UserProvince']] = {
        'name': data['UserProvince'],
        'count': 1
      }
    else:
      provinces[data['UserProvince']]['count'] = provinces[data['UserProvince']]['count'] + 1

  return provinces
