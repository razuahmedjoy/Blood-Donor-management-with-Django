import django_filters

from .models import *


class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ('blood_group', 'sub_district','union','ward_no')

DonorFilter.base_filters['sub_district'].label = ' উপজেলা '
DonorFilter.base_filters['union'].label = '   ইউনিয়ন   '
DonorFilter.base_filters['ward_no'].label = ' ওয়ার্ড নং  '
