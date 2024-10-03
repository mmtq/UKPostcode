from django.shortcuts import render, get_list_or_404, get_object_or_404
from Scotland import models
from django.utils.text import slugify
# Create your views here.

def scotland(request):
    districts_query = models.District.objects.all()
    context = {
        'districts': districts_query
    }
    return render(request, 'scotland/districts.html', context)

def district(request, district_slug):
    district_query = get_object_or_404(models.District, slug=district_slug)
    wards_query = models.Ward.objects.filter(district=district_query)
    context = {
        'district': district_query,
        'wards': wards_query
    }
    return render(request, 'scotland/wards.html', context)

def ward(request, district_slug, ward_slug):
    district_query = get_object_or_404(models.District, slug=district_slug)
    ward_query = get_object_or_404(models.Ward, slug=ward_slug, district=district_query)
    postcodes_query = models.PostcodeData.objects.filter(Ward=ward_query)
    context = {
        'ward': ward_query,
        'postcodes' : postcodes_query
    }
    return render(request, 'scotland/postcode.html', context)

def postcode(request, postcode):
    postcode = postcode.replace('-', ' ')
    area_tag = postcode[0: 2]
    district_tag = postcode[0: 3]
    postcode_query = get_object_or_404(models.PostcodeData, Postcode=postcode)
    ward = postcode_query.Ward
    ward_slug = slugify(ward)
    district = postcode_query.District
    district_slug = slugify(district)
    context = {
        'postcode': postcode_query,
        'ward': ward,
        'ward_slug': ward_slug,
        'district': district,
        'district_slug': district_slug,
        'area_tag': area_tag,
        'district_tag': district_tag
    }
    return render(request, 'scotland/single-postcode.html', context)