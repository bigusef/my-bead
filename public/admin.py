from django.contrib import admin
from .models import CompanyInfo, Telephones, Emails, Addresses, Mattress, Products, Manufacturer


admin.site.register(CompanyInfo)
admin.site.register(Telephones)
admin.site.register(Emails)
admin.site.register(Addresses)

admin.site.register(Mattress)
admin.site.register(Products)
admin.site.register(Manufacturer)

