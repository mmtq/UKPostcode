from django.urls import path, re_path
from NorthernIreland import views

urlpatterns = [
    path('nir/', views.NIR),
    re_path(r'^nir/(?P<postcode>[A-Z][A-Za-z0-9\-]+)/$', views.postcode, name='postcode'),
    re_path(r'^nir/(?P<district_slug>[a-z][A-Za-z0-9\-]*)/$', views.district, name='district'),
    path('nir/<str:district_slug>/<str:ward_slug>/', views.ward),
]