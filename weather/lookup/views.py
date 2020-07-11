from django.shortcuts import render
import json
import requests

def home(request):

    if request.method == "POST":
        zip_code = request.POST['zipcode']
        try:
            zip_code = int(zip_code)
        except ValueError:
            api = "Error"

        zip_code = str(zip_code)
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_code + "&distance=250&API_KEY=0915C9D7-2E23-4B4A-8A19-A8D577280FE6")    
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"    

        return render(request, 'index.html', {'api': api, 'len': range(len(api))}) 
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=85002&distance=250&API_KEY=0915C9D7-2E23-4B4A-8A19-A8D577280FE6")    
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"    

        return render(request, 'index.html', {'api': api, 'len': range(len(api))})

def about(request):
    return render(request, 'about.html', {})

