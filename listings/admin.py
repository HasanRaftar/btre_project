from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')

admin.site.register(Listing)