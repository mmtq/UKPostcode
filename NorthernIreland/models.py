from django.db import models

# Create your models here.

class district(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.name
    
class ward(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class PostcodeData(models.Model):
    postcode = models.CharField(max_length=100, db_index=True)
    normalized_postcode = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    easting = models.CharField(max_length=100)
    northing = models.CharField(max_length=100)
    grid_ref = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    district_code = models.CharField(max_length=100)
    ward_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    county_code = models.CharField(max_length=100)
    introduced = models.CharField(max_length=100)
    lower_layer_super_output_area = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    altitude = models.CharField(max_length=100)
    lsoa_code = models.CharField(max_length=100)
    msoa_code = models.CharField(max_length=100)
    middle_layer_super_output_area = models.CharField(max_length=100)
    parish_code = models.CharField(max_length=100)
    census_output_area = models.CharField(max_length=100)
    index_of_multiple_deprivation = models.CharField(max_length=100)
    quality = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)
    last_updated = models.CharField(max_length=100)
    postcode_area = models.CharField(max_length=100)
    postcode_district = models.CharField(max_length=100)
    police_force = models.CharField(max_length=100)
    water_company = models.CharField(max_length=100)
    plus_code = models.CharField(max_length=100)
    travel_to_work_area = models.CharField(max_length=100)
    itl_level_2 = models.CharField(max_length=100)
    itl_level_3 = models.CharField(max_length=100)
    distance_to_sea = models.CharField(max_length=100)
    census_output_area_2021 = models.CharField(max_length=100)
    constituency_code_2024 = models.CharField(max_length=100)
    constituency_name_2024 = models.CharField(max_length=100)

    def __str__(self):
        return self.postcode