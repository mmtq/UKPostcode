import requests
from django.shortcuts import render
from England.forms import FeedbackForm
from England import models as E
from Scotland import models as S
from wales import models as W
from NorthernIreland import models as N
import json
from django.http import JsonResponse

# def parcel_tracker(request):
#     api_key = 'asat_35f85fe1123348adaa4ff5189a678734'

#     # Endpoint URL
#     url = 'https://api.aftership.com/v4/trackings'

#     # Headers for authentication
#     headers = {
#         'Content-Type': 'application/json',
#         'aftership-api-key': api_key
#     }

#     # Example tracking number
#     tracking_number = 'FF924848872GB'

#     # API request
#     response = requests.get(f'{url}/{tracking_number}', headers=headers)

#     # Print the response
#     context = response.json()

#     return render(request, 'parcel.html', context)
def blog_view(request):
    return render(request, 'blog/uk-postcode.html')
def schools_view(request):
    feedback_message = None  # Initialize feedback_message as None
    flag = 0  # Initialize the flag as 0

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['text_field']
            q = q.upper()
            q = q.replace(" ", "%20")
            response = requests.get(f'https://www.doogal.co.uk/GetPostcode/{q}?output=json')
            
            try:
                feedback_message = response.json()

                # Check if feedback_message is empty or not as expected
                if not feedback_message or 'schools' not in feedback_message or not feedback_message['schools']:
                    feedback_message = "Sorry, no schools found."  # Set message for empty response
                    flag = 0  # Set the flag to 0 for empty response
                else:
                    flag = 1  # Set the flag to 1 if data is found

            except json.JSONDecodeError:
                # Handle JSON decode error
                feedback_message = "Please enter a valid UK postcode."
                flag = 0  # Set flag to 0 as no valid data was retrieved
            
            # Render the template with the form, feedback_message, and flag
            return render(request, 'england/school.html', {'form': form, 'feedback_message': feedback_message, 'flag': flag})
    else:
        form = FeedbackForm()

    # Render the template with the form, no feedback_message, and flag 0
    return render(request, 'england/school.html', {'form': form, 'flag': flag})

def busStops_view(request):
    feedback_message = None  # Initialize feedback_message as None
    flag = 0  # Initialize the flag as 0

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['text_field']
            q = q.upper()
            q = q.replace(" ", "%20")
            response = requests.get(f'https://www.doogal.co.uk/GetPostcode/{q}?output=json')
            
            try:
                feedback_message = response.json()

                # Check if feedback_message is empty or not as expected
                if not feedback_message or 'busStops' not in feedback_message or not feedback_message['busStops']:
                    feedback_message = "Sorry, no bus stops found."  # Set message for empty response
                    flag = 0  # Set the flag to 0 for empty response
                else:
                    flag = 1  # Set the flag to 1 if data is found

            except json.JSONDecodeError:
                # Handle JSON decode error
                feedback_message = "Please enter a valid UK postcode."
                flag = 0  # Set flag to 0 as no valid data was retrieved
            
            # Render the template with the form, feedback_message, and flag
            return render(request, 'england/busStops.html', {'form': form, 'feedback_message': feedback_message, 'flag': flag})
    else:
        form = FeedbackForm()

    # Render the template with the form, no feedback_message, and flag 0
    return render(request, 'england/busStops.html', {'form': form, 'flag': flag})

def search_view(request):
    key = request.GET.get('s','')
    search_term = key.replace(' ', '')
    search_type = request.GET.get('search_type', 'Postcode')
    if search_term and search_type == 'Postcode':
        england_postcodes = E.PostcodeData.objects.filter(normalized_postcode__icontains=search_term)
        scotland_postcodes = S.PostcodeData.objects.filter(normalized_postcode__icontains=search_term)
        wales_postcodes = W.PostcodeData.objects.filter(normalized_postcode__icontains=search_term)
        ni_postcodes = N.PostcodeData.objects.filter(normalized_postcode__icontains=search_term)
        postcodes = {}
        if england_postcodes.exists():
            postcodes['England'] = england_postcodes
            print(postcodes['England'])
        if scotland_postcodes.exists():
            postcodes['Scotland'] = scotland_postcodes
        if wales_postcodes.exists():
            postcodes['Wales'] = wales_postcodes
        if ni_postcodes.exists():
            postcodes['NorthernIreland'] = ni_postcodes

        context = {
            'postcodes': postcodes,
            'search_term': key
        }
        return render(request, 'search.html', context)
    search_term = key
    if search_term and search_type == 'Area':
        england_locations = {
            'county': E.County.objects.filter(name__icontains=search_term),
            'district': E.District.objects.filter(name__icontains=search_term),
            'ward': E.Ward.objects.filter(name__icontains=search_term)
        }

        scotland_locations = {
            'district': S.District.objects.filter(name__icontains=search_term),
            'ward': S.Ward.objects.filter(name__icontains=search_term)
        }

        wales_locations = {
            'district': W.district.objects.filter(name__icontains=search_term),
            'ward': W.ward.objects.filter(name__icontains=search_term)
        }

        ni_locations = {
            'district': N.district.objects.filter(name__icontains=search_term),
            'ward': N.ward.objects.filter(name__icontains=search_term)
        }
        flag = 0
        if len(england_locations['county']) + len(england_locations['district']) + len(england_locations['ward']) > 0 or len(scotland_locations['district']) + len(scotland_locations['ward']) > 0 or len(wales_locations['district']) + len(wales_locations['ward']) > 0 or len(ni_locations['district']) + len(ni_locations['ward']) > 0:
            flag = 1

        context = {
            'england': england_locations,
            'scotland': scotland_locations,
            'wales': wales_locations,
            'ni': ni_locations,
            'search_term': search_term,
            'flag': flag
        }

        print(context)
        return render(request, 'search.html', context)
def fetch_api_data(request):
    search_term = request.GET.get('search', '')

    if not search_term:
        return JsonResponse({'error': 'No search term provided'}, status=400)

    response = requests.get(f'https://www.doogal.co.uk/GetPostcode/{search_term}?output=json')
    response = response.json()

    return JsonResponse(response)