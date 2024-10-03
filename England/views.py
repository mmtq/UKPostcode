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
    area_tag = postcode[0: 2]
    district_tag = postcode[0: 3]
    postcode_query = get_object_or_404(models.PostcodeData, postcode=postcode)
    ward = postcode_query.ward
    ward_slug = slugify(ward)
    district = postcode_query.district
    district_slug = slugify(district)
    county = postcode_query.county
    county_slug = slugify(county)
    region = postcode_query.region
    region_slug = slugify(region)
    context = {
        'postcode': postcode_query,
        'ward_slug': ward_slug,
        'district_slug': district_slug,
        'county_slug': county_slug,
        'region_slug': region_slug,
        'area_tag': area_tag,
        'district_tag': district_tag
    }
    return render(request, 'england/single-postcode.html', context)

# from django.template.loader import render_to_string
# from django.http import HttpResponse
# from django.views import View
# from .models import Region, County, District, Ward, PostcodeData

# def generate_dynamic_sitemap():
#     urls = []
    
#     # Add static URLs
#     urls.append(('http://findpostcode.uk/', '2024-10-04', 'monthly', 1.0))
#     urls.append(('http://findpostcode.uk/england/', '2024-10-04', 'monthly', 0.8))

#     # Add dynamic URLs for Regions
#     regions = Region.objects.all()
#     for region in regions:
#         urls.append((f"http://findpostcode.uk/england/{region.slug}/", '2024-10-04', 'monthly', 0.6))
        
#         # Add Counties for each Region
#         counties = County.objects.filter(region=region)
#         for county in counties:
#             urls.append((f"http://findpostcode.uk/england/{region.slug}/{county.slug}/", '2024-10-04', 'monthly', 0.6))
            
#             # Add Districts for each County
#             districts = District.objects.filter(county=county)
#             for district in districts:
#                 urls.append((f"http://findpostcode.uk/england/{region.slug}/{county.slug}/{district.slug}/", '2024-10-04', 'monthly', 0.6))
                
#                 # Add Wards for each District
#                 wards = Ward.objects.filter(district=district)
#                 for ward in wards:
#                     urls.append((f"http://findpostcode.uk/england/{region.slug}/{county.slug}/{district.slug}/{ward.slug}/", '2024-10-04', 'monthly', 0.6))
    
    # Add Postcodes
    # postcodes = PostcodeData.objects.all()
    # for postcode in postcodes:
    #     urls.append((f"http://findpostcode.uk/england/{postcode.postcode}/", '2024-10-04', 'monthly', 0.6))
    
    return urls

# class DynamicSitemapView(View):
#     def get(self, request, *args, **kwargs):
#         urls = generate_dynamic_sitemap()
        
#         # Prepare the XML response
#         sitemap_content = render_to_string('england/sitemap.xml', {'urls': urls})
#         # return HttpResponse(sitemap_content, content_type='application/xml')
#         print(sitemap_content)
