from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'company','price')
	list_filter = ('created',)
	list_editable = ('price',)
	#prepopulated_fields = {'slug':('name',)}
	#raw_id_fields = ('company',)
	#actions = ('make_available',)

	# def make_available(self, request, queryset):
	#	rows = queryset.update(available=True)
	#	self.message_user(request, f'{rows} updated')
	# make_available.short_description = 'make all available'

