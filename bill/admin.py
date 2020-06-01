from django.contrib import admin
from .models import Bill
from .models import Order

admin.site.register(Bill)
admin.site.register(Order)
