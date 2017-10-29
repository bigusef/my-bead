from django.contrib import admin
from .models import CompanyInfo, Telephones, Emails, Adresses


admin.site.register(CompanyInfo)
admin.site.register(Telephones)
admin.site.register(Emails)
admin.site.register(Adresses)

