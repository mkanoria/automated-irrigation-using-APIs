Automated Irrigation System based on Weather Data
=====

A python implementation of an automated irrigation system based on weather data which can be used in a large scale case like a farm or even in a smale case like a home garden. GUI is implemented in *tkinter*

Uses Google's [**Geocoding API**](https://developers.google.com/maps/documentation/geocoding/start "Google Geocoding") and [**Dark Sky API**](https://darksky.net/dev "Dark Sky") to first get coordinates from an address and then get weather forecasts for those coordinates
Also, uses the [**Agro API**](https://home.agromonitoring.com/) to get information about the coordinates soil data, like soil temperature and moisture level

Users can user the GUI to enter an address and then the script checks the weather conditions and predicts how much water is required. It then switches on a solenoid valve for a duration that is appropriate.