from django.contrib import admin
from .models import Patients, Doctor
# Register your models here.

admin.site.register(Patients)
admin.site.register(Doctor)
