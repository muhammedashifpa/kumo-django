from django.contrib import admin
from .models import Brand,ProductTable,Size,SizeType,Images
# Register your models here.

class ProductImagesInline(admin.StackedInline):
    model = Images

@admin.register(ProductTable)
class ProductTableAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    prepopulated_fields = {'slug': ('gender','category','brand','product_name'), }


class SizeAdmin(admin.ModelAdmin):
    list_display = ['size','size_name']
    ordering = ['-size']


admin.site.register(Brand)
admin.site.register(Size,SizeAdmin)
admin.site.register(SizeType)

