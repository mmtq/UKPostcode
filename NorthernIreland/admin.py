from django.contrib import admin
from NorthernIreland import models
# Register your models here.

class districtAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

class wardAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'district')
    list_filter = ('district',)
    search_fields = ('name',)

class PostcodeDataAdmin(admin.ModelAdmin):
    list_display = ('postcode', 'ward', 'district')
    list_filter = ('ward', 'district')
    search_fields = ('postcode', 'ward', 'district')

admin.site.register(models.district, districtAdmin)
admin.site.register(models.ward, wardAdmin)
admin.site.register(models.PostcodeData, PostcodeDataAdmin)