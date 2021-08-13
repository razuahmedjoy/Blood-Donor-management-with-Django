import django_filters

from .models import *


class DonorFilter(django_filters.FilterSet):
    class Meta:
        model = Donor
        fields = ('blood_group', 'district')
