from django.contrib import admin
from . import models


admin.site.register(models.UserData)
admin.site.register(models.EventModel)
admin.site.register(models.EventReg)
admin.site.register(models.Participants)
admin.site.register(models.DigitalCertificate)
