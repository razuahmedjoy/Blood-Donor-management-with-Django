from django.contrib import admin

# Register your models here.
from .models import Donor,suruKotha,Volunteer,Mentor,Adviser,Blog,BLog_Category,shohojogi


class DonorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'blood_group',
                    'district', 'contact_no', 'email', 'status')

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name','designation','address','contact_no','is_active')
    list_editable = ('is_active',)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name','designation','address','contact_no','is_active')
    list_editable = ('is_active',)
class AdviserAdmin(admin.ModelAdmin):
    list_display = ('name','designation','address','contact_no','is_active')
    list_editable = ('is_active',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category')


admin.site.register(Donor, DonorAdmin)
admin.site.register(suruKotha)
admin.site.register(Volunteer,VolunteerAdmin)
admin.site.register(Mentor,MentorAdmin)
admin.site.register(Adviser,AdviserAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(BLog_Category)
admin.site.register(shohojogi)
