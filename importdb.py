import os
import django
import csv

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UKPostcode.settings')
django.setup()

from Scotland.models import PostcodeData

# Function to import CSV data into Django model
FIELD_MAP = {
    'Postcode': 'Postcode',
    'Latitude': 'Latitude',
    'Longitude': 'Longitude',
    'Easting': 'Easting',
    'Northing': 'Northing',
    'Grid Ref': 'Grid_Ref',
    'District': 'District',
    'Ward': 'Ward',
    'District Code': 'District_Code',
    'Ward Code': 'Ward_Code',
    'Country': 'Country',
    'County Code': 'County_Code',
    'Population': 'Population',
    'Households': 'Households',
    'Lower layer super output area': 'Lower_layer_super_output_area',
    'Rural/urban': 'Rural_urban',
    'Region': 'Region',
    'Altitude': 'Altitude',
    'LSOA Code': 'LSOA_Code',
    'MSOA Code': 'MSOA_Code',
    'Middle layer super output area': 'Middle_layer_super_output_area',
    'Parish Code': 'Parish_Code',
    'Census output area': 'Census_output_area',
    'Index of Multiple Deprivation': 'Index_of_Multiple_Deprivation',
    'Nearest station': 'Nearest_station',
    'Distance to station': 'Distance_to_station',
    'Postcode area': 'Postcode_area',
    'Postcode district': 'Postcode_district',
    'Police force': 'Police_force',
    'Water company': 'Water_company',
    'Plus Code': 'Plus_Code',
    'Travel To Work Area': 'Travel_To_Work_Area',
    'ITL level 2': 'ITL_level_2',
    'ITL level 3': 'ITL_level_3',
    'Distance to sea': 'Distance_to_sea',
    'Census output area 2021': 'Census_output_area_2021',
    'IMD decile': 'IMD_decile',
    'Constituency Code 2024': 'Constituency_Code_2024',
    'Constituency Name 2024': 'Constituency_Name_2024',
    'Property Type': 'Property_Type',
}

def import_csv_to_model(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:  # Use 'utf-8-sig' to handle BOM
        reader = csv.DictReader(csv_file)

        # Skip the header row
        next(reader)

        # Iterate over each row in the CSV
        for row in reader:
            try:
                # Convert all values to strings and map to model fields
                data = {FIELD_MAP.get(key, key): str(value) for key, value in row.items() if key in FIELD_MAP}
                # Insert the row into the model
                PostcodeData.objects.create(**data)
            except TypeError as e:
                # Log or print the error
                print(f"Error processing row {row}: {e}")
            except Exception as e:
                # Log or print any other errors
                print(f"Unexpected error processing row {row}: {e}")

# Path to your CSV file
csv_file_path = 'scotland.csv'

# Call the function to import data
import_csv_to_model(csv_file_path)


# import os
# import django

# # Set up Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UKPostcode.settings')
# django.setup()

# from England.models import PostcodeData

# PostcodeData.objects.all().delete()
