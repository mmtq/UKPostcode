from django.contrib import admin
from wales import models

# Register your models here.

class countyAdmin(admin.ModelAdmin):
    list_display = ['name']
class districtAdmin(admin.ModelAdmin):
    list_display = ['name', 'county']
    list_filter = ['county']

class wardAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']
    list_filter = ['district']
    search_fields = ['name']

class PostcodeDataAdmin(admin.ModelAdmin):
    list_display = ['postcode', 'ward', 'district']
    search_fields = ['postcode']
    list_filter = ['district', 'ward']

admin.site.register(models.PostcodeData, PostcodeDataAdmin)
admin.site.register(models.county, countyAdmin)
admin.site.register(models.district, districtAdmin)
admin.site.register(models.ward, wardAdmin)