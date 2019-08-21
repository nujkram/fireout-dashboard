from django.urls import path
from .modules.views import home as dashboard_home_view
from .modules.views import report as report_view


urlpatterns = [
  path('', dashboard_home_view.DashboardHomeView.as_view(), name='dashboard_home_view'),
  path('report/', report_view.DashboardReportView.as_view(), name='dashboard_report_view'),
]
