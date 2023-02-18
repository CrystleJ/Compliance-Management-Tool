from django.contrib import admin

# Register your models here.

from user.models import Country, City, NIST_171_Controls, NIST_172_Controls, NIST_53_Controls


admin.site.register(Country)
admin.site.register(City)

admin.site.register(NIST_171_Controls)
admin.site.register(NIST_172_Controls)
admin.site.register(NIST_53_Controls)


