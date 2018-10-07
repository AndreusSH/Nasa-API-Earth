from django.shortcuts import render
import requests

def home(request): 
    return render (request,'pictures/home.html')

def search(request):
    longitude =  request.POST['longitude']  
    latitude =  request.POST['latitude']
    search_date = request.POST['search_date']
    link = "https://api.nasa.gov/planetary/earth/imagery/?" 
    
    lon = "lon="+longitude  #    lon = "lon=100.75"#+longitude

    lat = "&lat="+latitude #"&lat=1.5"#+latitude
    date = "&date=2014-02-01"
    cloud = "&cloud_score=True&"
    api_key = "api_key=N3oZKz7mpvVKaUPnJ617Ov3cAeet9JurXRF5pqcx"

    #response = requests.get("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=N3oZKz7mpvVKaUPnJ617Ov3cAeet9JurXRF5pqcx")
    response = requests.get(link+lon+lat+date+cloud+api_key)
    data = response.json()
    return render (request, 'pictures/search.html', {'picture' : data['url'], 'longitude': longitude, 'latitude' : latitude})