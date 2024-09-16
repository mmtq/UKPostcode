"""
URL configuration for UKPostcode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search_view),
    path('blog/uk-postcode-format/', views.blog_view),
    path('api/fetch-data/', views.fetch_api_data, name='fetch_api_data'),
    path('', include('England.urls')),
    path('', include('Scotland.urls')),
    path('', include('wales.urls')),
    path('', include('NorthernIreland.urls')),
    # path('/parcel-tracker/', views.parcel_tracker, name='parcel-tracker'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
