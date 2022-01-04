from django.contrib import admin
from .models import Brand,ProductTable,Size,SizeType,Images,Coupon
# Register your models here.

class ProductImagesInline(admin.StackedInline):
    model = Images

@admin.register(ProductTable)
class ProductTableAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    list_display = ['id','product_name']
    prepopulated_fields = {'slug': ('gender','category','brand','product_name'), }


class SizeAdmin(admin.ModelAdmin):
    list_display = ['size','size_name']
    ordering = ['-size']
class CouponAdmin(admin.ModelAdmin):
    list_display = ['coupon_title','coupon_offer','coupon_code','is_valid']
    prepopulated_fields = {'coupon_code': ('coupon_title','coupon_offer'), }

admin.site.register(Brand)
admin.site.register(Size,SizeAdmin)
admin.site.register(SizeType)
admin.site.register(Coupon,CouponAdmin)

