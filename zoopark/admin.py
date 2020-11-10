from django.contrib import admin

# Register your models here.

from .models import Variety, Place, Human, Animal

admin.site.register(Variety)
admin.site.register(Place)
admin.site.register(Human)
admin.site.register(Animal)
