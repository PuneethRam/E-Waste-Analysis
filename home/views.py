from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
import os
import matplotlib.pyplot as plt
import io
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from django.core.files.storage import FileSystemStorage
import numpy as np
from PIL import Image
from .models import Resource
from .models import Recycle
from IPython import display
display.clear_output()

from transformers import BertTokenizer

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from geopy.distance import geodesic
from home.models import EwasteLocation
from .serializers import EwasteLocationSerializer
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

def nearest_ewaste_locations_page(request):
    print("pge")
    context = {}
    return render(request, "pages/location.html", context)



@csrf_exempt
def nearest_ewaste_locations(request):
    if request.method == 'POST':
        print("ewaste")
        user_latitude = float(request.POST.get('latitude'))
        user_longitude = float(request.POST.get('longitude'))

        user_location = (user_latitude, user_longitude)
        print(user_location)

        ewaste_locations = EwasteLocation.objects.all()
        nearest_locations = []
        print(ewaste_locations)

        for location in ewaste_locations:
            location_coordinates = (float(location.latitude), float(location.longitude))
            distance = geodesic(user_location, location_coordinates).kilometers
            lo=location.longitude
            la=location.latitude

            nearest_locations.append({
                'name': location.name,
                'address': location.address,
                'distance_km': distance,
                'latitude':la,
                'longitude':lo
            })

        nearest_locations.sort(key=lambda x: x['distance_km'])

        serializer = EwasteLocationSerializer(data=nearest_locations, many=True)
        if serializer.is_valid():
            return JsonResponse(serializer.data, safe=False)
        else:
            print("Not vlaid")

    return JsonResponse({'error': 'Invalid request method'}, status=400)






    




def index(request):
  context = {
    'segment': 'index'
  }
  return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/tables.html", context)

# Components
@login_required(login_url='/accounts/login/')
def bc_button(request):
  context = {
    'parent': 'basic_components',
    'segment': 'button'
  }
  return render(request, "pages/components/bc_button.html", context)

@login_required(login_url='/accounts/login/')
def bc_badges(request):
  context = {
    'parent': 'basic_components',
    'segment': 'badges'
  }
  return render(request, "pages/components/bc_badges.html", context)

@login_required(login_url='/accounts/login/')
def bc_breadcrumb_pagination(request):
  context = {
    'parent': 'basic_components',
    'segment': 'breadcrumbs_&_pagination'
  }
  return render(request, "pages/components/bc_breadcrumb-pagination.html", context)

@login_required(login_url='/accounts/login/')
def bc_collapse(request):
  context = {
    'parent': 'basic_components',
    'segment': 'collapse'
  }
  return render(request, "pages/components/bc_collapse.html", context)

@login_required(login_url='/accounts/login/')
def bc_tabs(request):
  context = {
    'parent': 'basic_components',
    'segment': 'navs_&_tabs'
  }
  return render(request, "pages/components/bc_tabs.html", context)

@login_required(login_url='/accounts/login/')
def bc_typography(request):
  context = {
    'parent': 'basic_components',
    'segment': 'typography'
  }
  return render(request, "pages/components/bc_typography.html", context)

@login_required(login_url='/accounts/login/')
def icon_feather(request):
  context = {
    'parent': 'basic_components',
    'segment': 'feather_icon'
  }
  return render(request, "pages/components/icon-feather.html", context)


# Forms and Tables
@login_required(login_url='/accounts/login/')
def form_elements(request):
  context = {
    'parent': 'form_components',
    'segment': 'form_elements'
  }
  return render(request, 'pages/form_elements.html', context)

@login_required(login_url='/accounts/login/')
def basic_tables(request):
  context = {
    'parent': 'tables',
    'segment': 'basic_tables'
  }
  return render(request, 'pages/tbl_bootstrap.html', context)

# Chart and Maps
@login_required(login_url='/accounts/login/')
def morris_chart(request):
  context = {
    'parent': 'chart',
    'segment': 'morris_chart'
  }
  return render(request, 'pages/chart-morris.html', context)

@login_required(login_url='/accounts/login/')
def google_maps(request):
  context = {
    'parent': 'maps',
    'segment': 'google_maps'
  }
  return render(request, 'pages/map-google.html', context)

# Authentication
class UserRegistrationView(CreateView):
  template_name = 'accounts/auth-signup.html'
  form_class = RegistrationForm
  success_url = '/accounts/login/'

class UserLoginView(LoginView):
  template_name = 'accounts/auth-signin.html'
  form_class = LoginForm

class UserPasswordResetView(PasswordResetView):
  template_name = 'accounts/auth-reset-password.html'
  form_class = UserPasswordResetForm

class UserPasswrodResetConfirmView(PasswordResetConfirmView):
  template_name = 'accounts/auth-password-reset-confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(PasswordChangeView):
  template_name = 'accounts/auth-change-password.html'
  form_class = UserPasswordChangeForm

def logout_view(request):
  logout(request)
  return redirect('/accounts/login/')

@login_required(login_url='/accounts/login/')
def profile(request):
  context = {
    'segment': 'profile',
  }
  return render(request, 'pages/profile.html', context)

@login_required(login_url='/accounts/login/')
def sample_page(request):
  context = {
    'segment': 'sample_page',
  }
  return render(request, 'pages/sample-page.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    recycling_requests=Recycle.objects.all()
    
    return render(request, 'pages/profile.html', {'recycling_requests': recycling_requests})

@login_required(login_url='/accounts/login/')
def recycle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        device_type = request.POST.get('deviceType')
        device_model = request.POST.get('deviceModel')
        weight_kg = request.POST.get('weight')
        picture = request.FILES['picture']
        pickup_type = request.POST.get('pickupType')
        pickup_date = request.POST.get('pickupDate')
        # Handle other form fields in a similar way

        # Create a new RecycleRequest object and save it to the database
        recycle_request = Recycle(
          username=name,
          city=city,
          device_type=device_type,
          device_model=device_model,
          weight_kg=weight_kg,
          picture = picture,
          pickup_type = pickup_type,
          pickup_date = pickup_date,
          stage=0
          )
        recycle_request.save()
    return render(request, 'pages/recycle.html')



@login_required(login_url='/accounts/login/')
def resource(request):
    last_uploaded_text = None
    if request.method == 'POST':
        name = request.POST.get('name')
        device_type = request.POST.get('deviceType')
        device_model = request.POST.get('deviceModel')
        weight_kg = request.POST.get('weight')
        search_word = device_model  # Replace 'your_search_word' with the word you want to search for

        # Initialize a list to store the corresponding "Product" values
        matching_products = []
        string="";device=""
        import pandas as pd
        a=pd.read_csv(r"home\recovery.csv")
        # Iterate through the rows and check if the word is present in the "device" column
        for index, row in a.iterrows():
            device_content = str(row['device']).lower()  # Convert to string in case it's not a string
            if search_word in device_content:
                matching_products.append(row['product'])
                device=device_content
                break

        # Print the corresponding "Product" values for rows where the word is found
        if matching_products:
            for product in matching_products:
                string+=product

        import openai

        api_key = ""
        prompt=	device+string+"/n"+"this data contain only the metals that are available and can be recovered from the electronic device(E waste) mentioned but not the amount. can you give me some approximate amount that can be extracted from single device seperated by commas. Give me in grams. Don't say It is not possible. I don't want any explanation. just give according to your knowledge"
              # Generate explanation using GPT-3 API
        openai.api_key = api_key
        response = openai.Completion.create(
                  engine="text-davinci-003",
                  prompt=prompt,
                  max_tokens=150,
                  stop=None,
                  temperature=0.7
        )

        explanation = response.choices[0].text.strip()
        print(explanation)

        resource = Resource(
          username=name,
          device_type=device_type,
          device_model=device_model,
          weight_kg=weight_kg,
          result=explanation
          )
        resource.save()
        last_uploaded_text = Resource.objects.latest('uploaded_at')
        
    return render(request, 'pages/resource.html',  {'latest_analysis_result': last_uploaded_text})
   

@login_required(login_url='/accounts/login/')
def credit(request):
    creditapprovescore = Recycle.objects.filter(stage=2)
    return render(request, 'pages/credit.html',{'cp': creditapprovescore})

@login_required(login_url='/accounts/login/')
def meta(request):
    return render(request, 'pages/meta.html')

@login_required(login_url='/accounts/login/')
def youtube(request):
    
    return render(request, 'pages/youtube.html')

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse



@login_required(login_url='/accounts/login/')
@csrf_exempt
def update_claim_credit(request):
    if request.method == 'POST':
        data = request.POST
        user_id = data.get('user_id')  # You should pass the user's ID in the request
        new_claim_credit = data.get('claim_credit')

        # Retrieve the CreditApprove object for the user
        credit_approve = get_object_or_404(Recycle, username=user_id)

        # Update the claim_credit value
        credit_approve.claim_credit = new_claim_credit
        credit_approve.save()

        return JsonResponse({'message': 'Claim Credit updated successfully'}, status=200)

    return JsonResponse({'message': 'Invalid request method'}, status=400)


