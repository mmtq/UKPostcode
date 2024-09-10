from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    code = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PostcodeData(models.Model):
    Postcode = models.TextField()
    Latitude = models.TextField()
    Longitude = models.TextField()
    Easting = models.TextField()
    Northing = models.TextField()
    Grid_Ref = models.TextField()
    District = models.TextField()
    Ward = models.TextField()
    District_Code = models.TextField()
    Ward_Code = models.TextField()
    Country = models.TextField()
    County_Code = models.TextField()
    Population = models.TextField()
    Households = models.TextField()
    Lower_layer_super_output_area = models.TextField()
    Rural_urban = models.TextField()
    Region = models.TextField()
    Altitude = models.TextField()
    LSOA_Code = models.TextField()
    MSOA_Code = models.TextField()
    Middle_layer_super_output_area = models.TextField()
    Parish_Code = models.TextField()
    Census_output_area = models.TextField()
    Index_of_Multiple_Deprivation = models.TextField()
    Nearest_station = models.TextField()
    Distance_to_station = models.TextField()
    Postcode_area = models.TextField()
    Postcode_district = models.TextField()
    Police_force = models.TextField()
    Water_company = models.TextField()
    Plus_Code = models.TextField()
    Travel_To_Work_Area = models.TextField()
    ITL_level_2 = models.TextField()
    ITL_level_3 = models.TextField()
    Distance_to_sea = models.TextField()
    Census_output_area_2021 = models.TextField()
    IMD_decile = models.TextField()
    Constituency_Code_2024 = models.TextField()
    Constituency_Name_2024 = models.TextField()
    Property_Type = models.TextField()

    def __str__(self):
        return self.Postcode
