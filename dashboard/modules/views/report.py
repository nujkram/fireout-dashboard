import pyrebase
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
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


class DashboardReportView(View):
  def get(self, request, *args, **kwargs):
    all_firebase_reports = db.child('Reports').get()
    reports = {}
    for report in all_firebase_reports.each():
      reports[report.key()] = report.val()

    context = {
      'page_title': 'FireOut: Reports',
      'location': 'reports',
      'reports': reports,
    }

    return render(request, 'dashboard/reports.html', context)
