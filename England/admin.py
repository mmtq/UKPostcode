from django.contrib import admin
from England import models
# Register your models here.
# @admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

class CountyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'region']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['region']

class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'county']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['county']
class WardAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'district']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_filter = ['district']

class PostcodeDataAdmin(admin.ModelAdmin):
    list_display = ['postcode', 'region', 'county', 'district', 'ward']
    search_fields = ['postcode']
    list_filter = ['region', 'county', 'district', 'ward']


admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.County, CountyAdmin)
admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.Ward, WardAdmin)
admin.site.register(models.PostcodeData, PostcodeDataAdmin)