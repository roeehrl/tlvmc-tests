from django.contrib import admin

from .models import Test, Tester, Patient

# Register your models here.

admin.site.register(Patient)
admin.site.register(Tester)
admin.site.register(Test)
