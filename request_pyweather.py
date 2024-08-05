import requests
import json
from datetime import datetime

headers = {
    'User-Agent': 'My Weather app',
    'From': 'kim.rosvoll@gmail.com'
}

url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Print the entire data for inspection
    #print("Response data:", json.dumps(data, indent=2))
    
    if 'properties' in data and 'timeseries' in data['properties']:
        timeseries = data['properties']['timeseries']
        
        # Check if timeseries is not empty
        #if timeseries:
            # Print all available timestamps
            #print("Available timestamps:")
            #for entry in timeseries:
                #print(entry['time'])
            
        # Find the closest timestamp to the desired one
        desired_time = datetime.fromisoformat("2024-08-05T19:00:00+00:00")
        closest_entry = min(timeseries, key=lambda x: abs(datetime.fromisoformat(x['time']) - desired_time))
        
        # Extract details from the closest entry
        details = closest_entry['data']['instant']['details']
        air_pressure = details['air_pressure_at_sea_level']
        air_temperature = details['air_temperature']
        cloud_area_fraction = details['cloud_area_fraction']
        relative_humidity = details['relative_humidity']
        wind_from_direction = details['wind_from_direction']
        wind_speed = details['wind_speed']
        
        # Print the extracted details
        print(f"Weather details for closest timestamp {closest_entry['time']}:")
        print(f"Air Pressure at Sea Level: {air_pressure} hPa")
        print(f"Air Temperature: {air_temperature} °C")
        print(f"Cloud Area Fraction: {cloud_area_fraction} %")
        print(f"Relative Humidity: {relative_humidity} %")
        print(f"Wind From Direction: {wind_from_direction} degrees")
        print(f"Wind Speed: {wind_speed} m/s")
        #else:
            #print("Timeseries is empty.")
    else:
        print("Properties or timeseries not found in the response data.")
else:
    print('Error fetching weather data')
    print(response.status_code)