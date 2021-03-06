from django.urls import path
from django.shortcuts import render
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    path("", CrashReportViews.as_view(), name="car-report"),
    path("data_report/", DataReport.as_view(), name="data-report"),
    path("uploadedpdf/", savefile, name="uploaded-pdf"),
    path("all_reports/", RequestReportView.as_view(), name="request-report"),
    path("automator/", automator, name="related_automator"),
    path("purchased_reports/", PurchasedReportView.as_view(), name="purchased_reports"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
