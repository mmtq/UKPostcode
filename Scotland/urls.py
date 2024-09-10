from django.urls import path, re_path
from Scotland import views

urlpatterns = [
    path('scotland/', views.scotland),
    re_path(r'^scotland/(?P<postcode>[A-Z][A-Za-z0-9\-]+)/$', views.postcode, name='postcode'),
    # Regex for region slugs (any alphanumeric with hyphens, lowercase start)
    re_path(r'^scotland/(?P<district_slug>[a-z][A-Za-z0-9\-]*)/$', views.district, name='region'),
    # path('scotland/<str:district_slug>/', views.district),
    path('scotland/<str:district_slug>/<str:ward_slug>/', views.ward),
]
