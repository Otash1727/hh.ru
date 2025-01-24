from django.contrib import admin
from .models import *
from .inlines import HistoryInline
# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display=['name','article','price','rating','quantity']
    #list_filter=['']


@admin.register(Accounting_Records)
class Accounting_RecordsAdmin(admin.ModelAdmin):
    list_display=['username','user_id']
    inlines=[HistoryInline]

