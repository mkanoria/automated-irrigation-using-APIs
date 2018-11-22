# TEST INPUT : 10996 Shoemake Ave, Modesto, CA 95358, USA
import requests, json, time
from keys import weather_key, geocoding_key, dark_sky_key, agro_key, polygon_id
from datetime import datetime
from water import water_requirement

# api request format: https://maps.googleapis.com/maps/api/geocode/json?parameters


def generate_value(city_name):
    #Weather API
    # code to generate the url
    API_KEY = weather_key()
    domain = "http://api.openweathermap.org/data/2.5/weather?q="
    url = domain + city_name + "&APPID=" + API_KEY

    #Geocoding API
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    GEOCODING_KEY = geocoding_key()
    words = city_name.split()
    address = ''
    for word in words:
        address += word + '+' 
    call = url + address + GEOCODING_KEY
    request = requests.get(call)
    r = request.json()
    lat = r["results"][0]["geometry"]["location"]['lat']
    lng = r["results"][0]["geometry"]["location"]['lng']

    #Dark Sky API
    DS_API_KEY = dark_sky_key()
    ds_domain = "https://api.darksky.net/forecast/" + DS_API_KEY
    ds_url =  ds_domain + str(lat) + "," + str(lng)
    request_ds = requests.get(ds_url)
    ds_data = request_ds.json()
    temp = ds_data['currently']['temperature']
    precip = ds_data['daily']['data'][0]['precipIntensityMax'] * 24
    print("\nThe Temperature at " + str(datetime.now()) + " is " + str(temp) + " F")
    dict1 = {"temp": temp}
    # change condition for return statement
    #pass dict into another function?
    
    #Using default value for polygon
    agro_domain = "http://api.agromonitoring.com/agro/1.0/soil?polyid="
    poly_id = polygon_id()
    agro_api_key = agro_key()
    agro_url = agro_domain + poly_id + "&appid=" + agro_api_key
    request_agro = requests.get(agro_url)
    agro_data = request_agro.json()
    soil_moisture = agro_data["moisture"]
    print("\nMositure is: " + str(soil_moisture*100) + "%")
    dict1["moisture"] = soil_moisture
    if(soil_moisture < 0.30):
        soil_type = "dry"
    elif (soil_moisture < 65):
        soil_type = "moist"
    else:
        soil_type = "wet"
        
    if(temp > 77):
        temp_condition = "hot"
    elif(temp>59):
        temp_condition = "medium"
    else:
        temp_condition = "low"

    WATER_REQUIRED = water_requirement(soil_type, temp_condition)
    dict1["WATER_REQUIRED"] = WATER_REQUIRED
    WATER_AFTER_PRECIP = WATER_REQUIRED - precip
    dict1["precip"] = precip
    dict1["WATER_AFTER_PRECIP"] = WATER_AFTER_PRECIP
    print("Water Required is: " + str(WATER_REQUIRED) + " mm")
    print("Rain predicted is: " + str(precip) + " mm")
    print("Water Required after rain is: " + str(WATER_AFTER_PRECIP) + " mm")

    if(WATER_AFTER_PRECIP<=0):
        dict1["WATER_AFTER_PRECIP"] = 0
    
    return dict1
    '''
    #weather API
    
    # code to generate and parse data from API
    request = requests.get(url)
    data = request.json()
    # weather_type = data["weather"][0]["main"]
    weather_description = data["weather"][0]["description"]
    weather_id = data["weather"][0]["id"]
    code_group = weather_id // 100
    print(weather_description + " " + str(weather_id) + " " + str(code_group))
    c = [2,3,5] #weather type --> thunderstorm, drizzle, rain
    if code_group in c:
        return 1
    return 0 
    '''
'''
def main():

    address = input("Enter the address of the place: ")
    i = 1
    
    # decide how many  times to call the API per hour
    while i: 
        generate_value(address)
        time.sleep(43200)

if __name__ == '__main__':
    main()
'''





    

