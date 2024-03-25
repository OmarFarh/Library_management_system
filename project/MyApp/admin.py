from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'LBMS'

class Book_DT(admin.ModelAdmin):
    list_display = ['Title' , 'Pages' , 'Price' , 'States']
    list_filter = ['States']
    search_fields = ['Title' , 'States']


admin.site.register(Book , Book_DT)
admin.site.register(Category)
