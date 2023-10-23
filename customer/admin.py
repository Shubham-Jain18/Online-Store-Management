from django.contrib import admin
from django.contrib.admin.sites import site
from customer.models import Customer_info

class customers(admin.ModelAdmin):
    list_display=('full_name','phone_number','address','key')

admin.site.register(Customer_info,customers)

