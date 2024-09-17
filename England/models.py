from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, null=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

class County(models.Model):
    name = models.CharField(max_length=100, null=False, db_index=True)
    slug = models.SlugField(max_length=100, null=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "County"
        verbose_name_plural = "Counties"

class District(models.Model):
    name = models.CharField(max_length=100, null=False, db_index=True)
    slug = models.SlugField(max_length=100, null=False)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

class Ward(models.Model):
    name = models.CharField(max_length=100, null=False, db_index=True)
    slug = models.SlugField(max_length=100, null=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ward"
        verbose_name_plural = "Wards"

class PostcodeData(models.Model):
    postcode = models.CharField(max_length=100, db_index=True)
    normalized_postcode = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    easting = models.CharField(max_length=100)
    northing = models.CharField(max_length=100)
    grid_ref = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    district_code = models.CharField(max_length=100)
    ward_code = models.CharField(max_length=100)
    county_code = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    parish = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    households = models.CharField(max_length=100)
    built_up_area = models.CharField(max_length=100)
    built_up_subdivision = models.CharField(max_length=100)
    lower_layer_super_output_area = models.CharField(max_length=100)
    rural_urban = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    altitude = models.CharField(max_length=100)
    lsoa_code = models.CharField(max_length=100)
    local_authority = models.CharField(max_length=100)
    msoa_code = models.CharField(max_length=100)
    middle_layer_super_output_area = models.CharField(max_length=100)
    parish_code = models.CharField(max_length=100)
    constituency_code = models.CharField(max_length=100)
    index_of_multiple_deprivation = models.CharField(max_length=100)
    nearest_station = models.CharField(max_length=100)
    distance_to_station = models.CharField(max_length=100)
    postcode_area = models.CharField(max_length=100)
    postcode_district = models.CharField(max_length=100)
    police_force = models.CharField(max_length=100)
    water_company = models.CharField(max_length=100)
    plus_code = models.CharField(max_length=100)
    sewage_company = models.CharField(max_length=100)
    itl_level_2 = models.CharField(max_length=100)
    itl_level_3 = models.CharField(max_length=100)
    distance_to_sea = models.CharField(max_length=100)
    lsoa21_code = models.CharField(max_length=100)
    lower_layer_super_output_area_2021 = models.CharField(max_length=100)
    msoa21_code = models.CharField(max_length=100)
    middle_layer_super_output_area_2021 = models.CharField(max_length=100)
    imd_decile = models.CharField(max_length=100)
    constituency_code_2024 = models.CharField(max_length=100)
    constituency_name_2024 = models.CharField(max_length=100)
    property_type = models.CharField(max_length=100)

    def __str__(self):
        return self.postcode
