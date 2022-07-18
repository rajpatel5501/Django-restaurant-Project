from django.contrib import admin
from store.models import Product


class ProductsModelAdmin(admin.ModelAdmin):

  list_display = ('id', 'name', 'description', 'price', 'user')
  list_filter = ('user',)

  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ( 'name', 'description', 'price', 'user'),
      }),
  )
  search_fields = ('name',)
  ordering = ('name', 'description')
  filter_horizontal = ()



admin.site.register(Product , ProductsModelAdmin)