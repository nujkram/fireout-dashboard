import pyrebase
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)

auth = firebase.auth()
db = firebase.database()


def noquote(s):
  return s


pyrebase.pyrebase.quote = noquote


class DashboardReportView(View):
  def get(self, request, *args, **kwargs):
    firebase_reports = db.child('Reports').get()
    reports = {}
    for report in firebase_reports.each():
      reports[report.key()] = report.val()

    context = {
      'page_title': 'FireOut: Reports',
      'location': 'reports',
      'reports': reports,
    }

    return render(request, 'dashboard/reports/home.html', context)


class DashboardReportDetailView(View):
  def get(self, request, *args, **kwargs):
    report_id = kwargs['id']
    firebase_report = db.child('Reports').order_by_key().equal_to(report_id).get()

    context = {
      'page_title': 'FireOut Report Detail',
      'location': 'report',
      'report': firebase_report.val(),
    }

    return render(request, 'dashboard/reports/detail.html', context)


class DashboardReportApi(APIView):
  def get(self, request, *args, **kwargs):
    firebase_reports = db.child('Reports').get()
    reports = {}
    for report in firebase_reports.each():
      reports[report.key()] = report.val()

    return JsonResponse(reports)
