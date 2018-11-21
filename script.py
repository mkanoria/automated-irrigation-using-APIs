#TODO display the coordinates using geocoding API
#TODO soil moisture data from Agro API
import requests, json, time
from keys import weather_key, geocoding_key, dark_sky_key

# api request format: https://maps.googleapis.com/maps/api/geocode/json?parameters


def generate_value(city_name):
    # code to generate the url
    API_KEY = weather_key()
    domain = "http://api.openweathermap.org/data/2.5/weather?q="
    url = domain + city_name + "&APPID=" + API_KEY

    #Geocoding
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
    print(str(temp) + " F")
    if(temp > 76.6):
        return 1
    else:
        return 0

    #weather API
    '''
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

def main():
    address = input("Enter the address of the place: ")
    i = 0
    generate_value(address)

    # decide how many  times to call the API per hour
    while i < 10: 
        generate_value(address)
        i += 1
        time.sleep(10)

if __name__ == '__main__':
    main()






    

