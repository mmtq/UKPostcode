from django.shortcuts import render, get_object_or_404
from NorthernIreland import models
from django.utils.text import slugify

# Create your views here.

def NIR(request):
    districts_query = models.district.objects.all()
    context = {
        'districts': districts_query
    }
    return render(request, 'bt/districts.html', context)

def district(request, district_slug):
    district_query = get_object_or_404(models.district, slug=district_slug)
    wards_query = models.ward.objects.filter(district=district_query)
    context = {
        'district': district_query,
        'wards': wards_query
    }
    return render(request, 'bt/ward.html', context)

def ward(request, district_slug, ward_slug):
    district_query = get_object_or_404(models.district, slug=district_slug)
    ward_query = get_object_or_404(models.ward, slug=ward_slug, district=district_query)
    postcodes_query = models.PostcodeData.objects.filter(ward=ward_query)
    context = {
        'ward': ward_query,
        'postcodes' : postcodes_query
    }
    return render(request, 'bt/postcode.html', context)

def postcode(request, postcode):
    postcode = postcode.replace('-', ' ')
    area_tag = postcode[0: 2]
    district_tag = postcode[0: 3]
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
        'area_tag': area_tag,
        'district_tag': district_tag
    }
    return render(request, 'bt/single-postcode.html', context)