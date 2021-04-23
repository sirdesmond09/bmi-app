from bmi.models import Bmi
from django.contrib import admin

# Register your models here.
#username: bmiadmin
#password: bmiadmin123
@admin.register(Bmi)
class BmiAdmin(admin.ModelAdmin):
    list_display = ['user', 'height', 'weight', 'bmi', 'date']