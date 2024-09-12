from django.urls import path, re_path
from wales import views

urlpatterns = [
    path('wales/', views.wales),
    re_path(r'^wales/(?P<postcode>[A-Z][A-Za-z0-9\-]+)/$', views.postcode, name='postcode'),
    re_path(r'^wales/(?P<county_slug>[a-z][A-Za-z0-9\-]*)/$', views.county, name='county'),
    path('wales/<county_slug>/<district_slug>/', views.district, name='district'),
    path('wales/<county_slug>/<district_slug>/<ward_slug>/', views.ward, name='ward'),
]
