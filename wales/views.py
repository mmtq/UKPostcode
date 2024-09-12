from django.shortcuts import render, get_object_or_404
from wales import models
from django.utils.text import slugify
# Create your views here.

def wales(request):
    county_query = models.county.objects.all()
    context = {
        'counties': county_query
    }
    return render(request, 'wales/county.html', context)

def county(request, county_slug):
    county_query = get_object_or_404(models.county, slug=county_slug)
    district_query = models.district.objects.filter(county=county_query)
    context = {
        'county': county_query,
        'districts': district_query
    }
    return render(request, 'wales/district.html', context)

def district(request, county_slug, district_slug):
    county_query = get_object_or_404(models.county, slug=county_slug)
    district_query = get_object_or_404(models.district, slug=district_slug, county=county_query)
    ward_query = models.ward.objects.filter(district=district_query)
    context = {
        'district': district_query,
        'county': county_query,
        'wards': ward_query
    }
    return render(request, 'wales/ward.html', context)

def ward(request, county_slug, district_slug, ward_slug):
    county_query = get_object_or_404(models.county, slug=county_slug)
    district_query = get_object_or_404(models.district, slug=district_slug, county=county_query)
    ward_query = get_object_or_404(models.ward, slug=ward_slug, district=district_query)
    postcodes_query = models.PostcodeData.objects.filter(ward=ward_query)
    print(postcodes_query)
    context = {
        'ward': ward_query,
        'district': district_query,
        'county': county_query,
        'postcodes' : postcodes_query
    }
    return render(request, 'wales/postcode.html', context)

def postcode(request, postcode):
    postcode = postcode.replace('-', ' ')
    postcode_query = get_object_or_404(models.PostcodeData, postcode=postcode)
    ward = postcode_query.ward
    ward_slug = slugify(ward)
    district = postcode_query.district
    district_slug = slugify(district)

    context = {
        'postcode': postcode_query,
        'ward': ward,
        'ward_slug': ward_slug,
        'district': district,
        'district_slug': district_slug,
    }
    return render(request, 'wales/single-postcode.html', context)