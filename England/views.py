from django.shortcuts import render, get_object_or_404, get_list_or_404
from England import models
from England.forms import FeedbackForm
import requests
from django.utils.text import slugify
# Create your views here.

def home(request):
    return render(request, 'home.html')

def england(request):
    regions_query = models.Region.objects.all()
    context = {
        'regions': regions_query
    }
    return render(request, 'england/region.html', context)

def region(request, region_slug):
    county_query = models.County.objects.filter(region__slug=region_slug)
    region_query = get_object_or_404(models.Region, slug=region_slug)
    context = {
        'counties': county_query,
        'region': region_query
    }
    return render(request, 'england/county.html', context)

def county(request, region_slug, county_slug):
    region_query = get_object_or_404(models.Region, slug=region_slug)
    county_query = get_object_or_404(models.County, slug=county_slug, region=region_query)
    district_query = models.District.objects.filter(county=county_query)
    context = {
        'county': county_query,
        'region': region_query,
        'districts': district_query
    }
    return render(request, 'england/district.html', context)

def district(request, region_slug, county_slug, district_slug):
    region_query = get_object_or_404(models.Region, slug=region_slug)
    county_query = get_object_or_404(models.County, slug=county_slug, region=region_query)
    district_query = get_object_or_404(models.District, slug=district_slug, county=county_query)
    ward_query = models.Ward.objects.filter(district=district_query)
    context = {
        'district': district_query,
        'county': county_query,
        'region': region_query,
        'wards': ward_query
    }
    return render(request, 'england/ward.html', context)

def ward(request, region_slug, county_slug, district_slug, ward_slug):
    region_query = get_object_or_404(models.Region, slug=region_slug)
    county_query = get_object_or_404(models.County, slug=county_slug, region=region_query)
    district_query = get_object_or_404(models.District, slug=district_slug, county=county_query)
    ward_query = get_object_or_404(models.Ward, slug=ward_slug, district=district_query)
    postcodes_query = models.PostcodeData.objects.filter(ward=ward_query)
    context = {
        'ward': ward_query,
        'district': district_query,
        'county': county_query,
        'region': region_query,
        'postcodes' : postcodes_query
    }
    return render(request, 'england/postcode.html', context)

def postcode(request, postcode):
    postcode = postcode.replace('-', ' ')
    postcode_query = get_object_or_404(models.PostcodeData, postcode=postcode)
    ward = postcode_query.ward
    ward_slug = slugify(ward)
    district = postcode_query.district
    district_slug = slugify(district)
    county = postcode_query.county
    county_slug = slugify(county)
    region = postcode_query.region
    region_slug = slugify(region)
    # random = models.PostcodeData.objects.order_by('?')[:9]
    # for field in postcode_query._meta.fields:
    #     field_name = field.name
    #     field_value = getattr(postcode_query, field_name)
    #     print(f"{field_name}: {field_value}")

    context = {
        'postcode': postcode_query,
        'ward_slug': ward_slug,
        'district_slug': district_slug,
        'county_slug': county_slug,
        'region_slug': region_slug,
    }
    return render(request, 'england/single-postcode.html', context)