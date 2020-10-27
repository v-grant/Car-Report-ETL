from django.contrib import admin
from .models import CrashReport
from .models import RequestReport

admin.site.register(CrashReport)
admin.site.register(RequestReport)
