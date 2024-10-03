from django.urls import path, re_path
from . import views
from UKPostcode import views as p_views

urlpatterns = [
    path('', views.home),
    path('england/', views.england),
    # Regex for postcodes starting with an uppercase letter (A-Z)
    re_path(r'^england/(?P<postcode>[A-Z][A-Za-z0-9\-]+)/$', views.postcode, name='postcode'),
    # Regex for region slugs (any alphanumeric with hyphens, lowercase start)
    re_path(r'^england/(?P<region_slug>[a-z][A-Za-z0-9\-]*)/$', views.region, name='region'),
    path('england/<str:region_slug>/<str:county_slug>/', views.county),
    path('england/<str:region_slug>/<str:county_slug>/<str:district_slug>/', views.district),
    path('england/<str:region_slug>/<str:county_slug>/<str:district_slug>/<str:ward_slug>/', views.ward),
    path('nearby-schools/', p_views.schools_view, name='feedback'),
    path('nearby-bus-stops/', p_views.busStops_view, name='feedback'),
    # path('england/<str:postcode>/', views.postcode),
    path('sitemap.xml', views.DynamicSitemapView.as_view(), name='sitemap'),

    
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

