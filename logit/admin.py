from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Symptom)
admin.site.register(models.Medication)
admin.site.register(models.Diagnosis)
