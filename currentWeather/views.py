from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
import json

from .models import Location, customUser

#wunderground API key
key = '14dbb9fdae1464b3'

#weather report view
def weather(request):
    if request.method == 'POST':
        currentUser = request.POST['currentUser']
        users = customUser.objects.all()
        flag = 0
        
        for user in users:
            if user.username == currentUser:
                flag = 1
                
        #creates new user if not already existing
        if flag == 0:
            newUser = customUser(username=currentUser)
            newUser.save()

    locations = Location.objects.filter(user=currentUser).order_by('name')

    #updates weather information for each of the user's locations
    for location in locations:
        zipCode = location.zipCode
        url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zipCode + '.json'
        f = urlopen(url)
        parsed_json = json.loads(f.readall().decode('utf-8'))
        location.temperature = parsed_json['current_observation']['temperature_string']
        location.condition = parsed_json['current_observation']['weather']
        location.save()
        f.close()
        
    return render(request, 'currentWeather/weather.html', {'locations' : locations, 'currentUser' : currentUser})

#redirect page to confirm location added or pre-existing
def newLocation(request):
    if request.method == 'POST':
        zipCodeInput = request.POST['zipCodeInput']
        currentUser = request.POST['currentUser']
        locations = Location.objects.filter(user=currentUser).order_by('name')
        flag = 0

        #checks for pre-existing location entry
        for location in locations:
            if location.zipCode == zipCodeInput:
                flag = 1

        #retrieves weather information for new location
        if flag == 0:
            url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zipCodeInput + '.json'
            f = urlopen(url)
            parsed_json = json.loads(f.readall().decode('utf-8'))
            
            #checks for zip code validity
            #by checking for error key
            if 'error' in parsed_json['response']:
                flag = 2
            else:
                city = parsed_json['location']['city']
                state = parsed_json['location']['state']
                newName = city + ', ' + state
                newTemp = parsed_json['current_observation']['temperature_string']
                newCondition = parsed_json['current_observation']['weather']
                newLocation = Location(user=currentUser, name=newName, zipCode=zipCodeInput, temperature=newTemp, condition=newCondition)
                newLocation.save()
            f.close()
            
    return render(request, 'currentWeather/newLocation.html', {'flag' : flag, 'currentUser' : currentUser})

#login page
def login(request):
    return render(request, 'currentWeather/login.html', {})
