from django.contrib import admin

# Register your models here.
from .models import *

class CouponAdmin(admin.ModelAdmin):
    list_filter = ("reduction",)
    list_display = ("code", "reduction",)

admin.site.register(Coupon,CouponAdmin)
admin.site.register(Transaction)
