from django.contrib import admin
from homeproduct.models import homeProduct
class HomeAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_img')
admin.site.register(homeProduct,HomeAdmin)
# Register your models here.
