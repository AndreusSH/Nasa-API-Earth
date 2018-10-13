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

    lat = "&lat="+latitude+"&date=" #"&lat=1.5"#+latitude
    date = search_date #2014-02-01
    cloud = "&cloud_score=True&"
    api_key = "get_your_own_Api_following_the_README.md"

    #response = requests.get("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=N3oZKz7mpvVKaUPnJ617Ov3cAeet9JurXRF5pqcx")
    response = requests.get(link+lon+lat+date+cloud+api_key)
    data = response.json()
    if  request.method == 'POST':
        try:
            return render (request, 'pictures/search.html', {'picture' : data['url'], 'longitude': longitude, 'latitude' : latitude, 'date': date})
        except:
            return render(request, 'pictures/home.html', {'error': 'You need to specify both latitude and longitude'})
        
        
    

     
      #  return render(request, 'pictures/search.html', {'error': 'xxxxxxxx'})
   
     
       # return render(request, 'pictures/home.html', {'error': 'You need to specify both latitude and longitude'})
