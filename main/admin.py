from django.contrib import admin
from django.contrib.admin import register
from django import forms

from main.models import Category, Product, Order, OrderProduct


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']


# @register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_filter = ['category']
    search_fields = ['name']


class ProductFormSet(forms.BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            quantity = form.cleaned_data['quantity']
            if quantity < 0:
                raise forms.ValidationError('Wrong quantity')
        return super().clean()

    # def clean2(self):
    #     count = 0
    #     for form in self.forms:
    #         is_main = form.cleaned_data['is_main']
    #         if is_main:
    #             count += 1
    #     if count > 1:
    #         raise ...
    #     return super().clean()


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    formset = ProductFormSet
    fields = ['product', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
