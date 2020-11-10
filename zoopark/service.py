from django_filters import rest_framework as filters
from .models import Variety, Place, Human, Animal


class AnimalFilter(filters.FilterSet):
    month_human = filters.RangeFilter()  # RangeFilter - дает возможность ставить мин, макc
    filter_fields = ("place__length", "place__width")

    class Meta:
        model = Animal
        fields = ['month_human', 'place__length', 'place__width']  # поля, по которым надо фильтровать

# class PlaceFilter(filters.FilterSet):
#     two = filters.RangeFilter() # минимум 2 вида
#     min_variety = filters.NumberFilter(field_name="")
#     # filter_fields = ("animal__id", "variety__id")
#
#     class Meta:
#         model = Place
#         fields = ['animal__id', 'variety__id']
