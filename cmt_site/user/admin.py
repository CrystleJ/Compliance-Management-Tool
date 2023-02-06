from django.contrib import admin

# Register your models here.

from user.models import Country, City


admin.site.register(Country)
admin.site.register(City)
