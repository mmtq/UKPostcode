from django.contrib import admin
from Scotland import models

# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

class WardAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'district']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['district']

class PostcodeDataAdmin(admin.ModelAdmin):
    list_display = ['Postcode', 'Ward', 'District']
    search_fields = ['Postcode']
    list_filter = ['District', 'Ward']

admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.Ward, WardAdmin)
admin.site.register(models.PostcodeData, PostcodeDataAdmin)