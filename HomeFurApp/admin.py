from django.contrib import admin
from .models import CustomerAuth, AdminProducts
# Register your models here.

admin.site.register(CustomerAuth)
admin.site.register(AdminProducts)