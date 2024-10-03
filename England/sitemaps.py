from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Region, County, District, Ward, PostcodeData

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ['home', 'england', 'nearby-schools', 'nearby-bus-stops']

    def location(self, item):
        return reverse(item)

class RegionSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Region.objects.all()

    def location(self, obj):
        return reverse('region', args=[obj.slug])

class CountySitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return County.objects.all()

    def location(self, obj):
        return reverse('county', args=[obj.region.slug, obj.slug])

class DistrictSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return District.objects.all()

    def location(self, obj):
        return reverse('district', args=[obj.county.region.slug, obj.county.slug, obj.slug])

class WardSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Ward.objects.all()

    def location(self, obj):
        return reverse('ward', args=[obj.district.county.region.slug, obj.district.county.slug, obj.district.slug, obj.slug])

class PostcodeSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return PostcodeData.objects.all()

    def location(self, obj):
        return reverse('postcode', args=[obj.postcode])
