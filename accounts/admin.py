from django.contrib import admin

import accounts.models as m
# Register your models here.

admin.site.register(m.CustomUser)