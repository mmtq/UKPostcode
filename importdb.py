# import os
# import django
# import csv

# # Set up Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UKPostcode.settings')
# django.setup()

# from NorthernIreland.models import PostcodeData
# # Function to import CSV data into Django model
# FIELD_MAP = {
#     'Postcode': 'postcode',
#     'Latitude': 'latitude',
#     'Longitude': 'longitude',
#     'Easting': 'easting',
#     'Northing': 'northing',
#     'Grid Ref': 'grid_ref',
#     'District': 'district',
#     'Ward': 'ward',
#     'District Code': 'district_code',
#     'Ward Code': 'ward_code',
#     'Country': 'country',
#     'County Code': 'county_code',
#     'Lower layer super output area': 'lower_layer_super_output_area',
#     'Region': 'region',
#     'Altitude': 'altitude',
#     'LSOA Code': 'lsoa_code',
#     'MSOA Code': 'msoa_code',
#     'Middle layer super output area': 'middle_layer_super_output_area',
#     'Parish Code': 'parish_code',
#     'Census output area': 'census_output_area',
#     'Index of Multiple Deprivation': 'index_of_multiple_deprivation',
#     'Quality': 'quality',
#     'User Type': 'user_type',
#     'Last updated': 'last_updated',
#     'Postcode area': 'postcode_area',
#     'Postcode district': 'postcode_district',
#     'Police force': 'police_force',
#     'Water company': 'water_company',
#     'Plus Code': 'plus_code',
#     'Travel To Work Area': 'travel_to_work_area',
#     'ITL level 2': 'itl_level_2',
#     'ITL level 3': 'itl_level_3',
#     'Distance to sea': 'distance_to_sea',
#     'Census output area 2021': 'census_output_area_2021',
#     'Constituency Code 2024': 'constituency_code_2024',
#     'Constituency Name 2024': 'constituency_name_2024'
# }



# def import_csv_to_model(csv_file_path):
#     with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:  # Use 'utf-8-sig' to handle BOM
#         reader = csv.DictReader(csv_file)

#         # Skip the header row
#         next(reader)

#         # Iterate over each row in the CSV
#         for row in reader:
#             try:
#                 # Convert all values to strings and map to model fields
#                 data = {FIELD_MAP.get(key, key): str(value) for key, value in row.items() if key in FIELD_MAP}
#                 # Insert the row into the model
#                 PostcodeData.objects.create(**data)
#             except TypeError as e:
#                 # Log or print the error
#                 print(f"Error processing row {row}: {e}")
#             except Exception as e:
#                 # Log or print any other errors
#                 print(f"Unexpected error processing row {row}: {e}")

# # Path to your CSV file
# csv_file_path = 'bt.csv'

# # Call the function to import data
# import_csv_to_model(csv_file_path)


# # import os
# # import django

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UKPostcode.settings')
# # django.setup()

# # from England.models import PostcodeData

# # PostcodeData.objects.all().delete()


import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UKPostcode.settings')  # Replace with your project name
django.setup()

from Scotland.models import PostcodeData

# The actual script logic
def populate_normalized_postcode():
    postcodes = PostcodeData.objects.all()
    count = postcodes.count()
    print(f'Found {count} postcodes to update.')

    for postcode in postcodes:
        normalized = postcode.Postcode.replace(' ', '')
        postcode.normalized_postcode = normalized
        postcode.save(update_fields=['normalized_postcode'])

    print('Successfully populated normalized_postcode field.')

if __name__ == '__main__':
    populate_normalized_postcode()
