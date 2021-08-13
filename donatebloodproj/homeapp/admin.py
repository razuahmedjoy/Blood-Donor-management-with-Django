from django.contrib import admin

# Register your models here.
from .models import Donor


class DonorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'blood_group',
                    'district', 'contact_no', 'email', 'status')


admin.site.register(Donor, DonorAdmin)
