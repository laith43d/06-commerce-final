from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from commerce.models import Product, Order, Item, Address, OrderStatus, ProductImage, City, Category, Vendor, Merchant, \
    Label


class InlineProductImage(admin.TabularInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage,]
    list_display = ('id', 'name', 'qty', 'description', 'cost', 'price', 'discounted_price')
    list_filter = ('category', 'label', 'merchant', 'vendor')
    search_fields = ('name', 'qty', 'description', 'cost', 'price', 'discounted_price', 'merchant__name')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(Address)
admin.site.register(OrderStatus)
# admin.site.register(ProductImage)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(Merchant)
admin.site.register(Label)
