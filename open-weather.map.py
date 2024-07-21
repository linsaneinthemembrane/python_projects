import pprint
import requests
import sys
import csv

api_key = "48bb8ddd42dc7ad0c83c7ef79d2016f8"

geo_URL = 'http://api.openweathermap.org/geo/1.0/direct'

forecast_URL = 'http://api.openweathermap.org/data/2.5/forecast'


list_cities = ['Buenos Aires, Argentina',
  'Guangzhou, China',
  'Wichita, Kansas',
  'Niskayuna, New York',
  'Gwangmyeong, South Korea',
  'Taipei, Taiwan',
  'Nanaimo, British Columbia',
  'Chennai, India',
  'Barrington, Illinois',
  'Littleton, Colorado',
  'Peterhead, Scotland',
  'Vizag, India',
  'Des Moines, Iowa',
  'Beijing, China',
  'Killeen, Texas',
  'Morehead City, North Carolina'] 
  

    
def get_city_coordinates(city, api_key):
    geo = f'{geo_URL}?q={city}&limit=1&appid={api_key}'
    resp = requests.get(geo)
    if resp.status_code != 200:
        print(f'Error geocoding {city}: {resp.status_code}')
        sys.exit(1)
    json = resp.json()
    if len(json) == 0:
        print(f'Error locating city {city}')
        sys.exit(2)
    lat = json[0]['lat']
    lon = json[0]['lon']
    return lat, lon

def get_forecast(lat, lon, api_key):
    forecast = f'{forecast_URL}?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    resp = requests.get(forecast)
    if resp.status_code != 200:
        print(f'Error retrieving forecast data: {resp.status_code}')
        sys.exit(3)
    return resp.json()

def get_temp(data):
    daily_temps = [[], [], [], []]
    current_day = 0
    
    # Find the first block with time 00:00:00
    start_index = 0
    for i, entry in enumerate(data['list']):
        if '00:00:00' in entry['dt_txt']:
            start_index = i
            break

    # Collect temperatures from the first block of tomorrow
    for i in range(start_index, len(data['list'])):
        entry = data['list'][i]
        date, time = entry['dt_txt'].split(' ')
        temp_min = entry['main']['temp_min']
        temp_max = entry['main']['temp_max']

        daily_temps[current_day].append((temp_min, temp_max))

        # Move to the next day after collecting 8 blocks (24 hours)
        if len(daily_temps[current_day]) == 8:
            current_day += 1
            if current_day > 3:
                break

    # Compute min and max temperatures
    min_temps = [min(day, key=lambda x: x[0])[0] for day in daily_temps if day]
    max_temps = [max(day, key=lambda x: x[1])[1] for day in daily_temps if day]
    min_avg = sum(min_temps) / len(min_temps)
    max_avg = sum(max_temps) / len(max_temps)

    return min_temps, max_temps, min_avg, max_avg

def write_csv(cities):
    with open('temp.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        header = ['City', 'Min 1', 'Max 1', 'Min 2',
                  'Max 2', 'Min 3', 'Max 3', 'Min 4',
                  'Max 4', 'Min Avg', 'Max Avg']
        writer.writerow(header)
        for city, min_temps, max_temps, min_avg, max_avg in cities:
            row = [city]
            
            # Append min and max temperatures in pairs
            for i in range(4):
                if i < len(min_temps):
                    row.append(f"{min_temps[i]:.2f}")
                if i < len(max_temps):
                    row.append(f"{max_temps[i]:.2f}")
                    
            # Append averages
            row.append(f"{min_avg:.2f}")
            row.append(f"{max_avg:.2f}")
            
            writer.writerow(row)
            
# create empty list to hold data 
city_data = []

for city in list_cities:
    lat, lon = get_city_coordinates(city, api_key)
    forecast_data = get_forecast(lat, lon, api_key)
    min_temps, max_temps, min_avg, max_avg = get_temp(forecast_data)
    city_data.append((city, min_temps, max_temps, min_avg, max_avg))
    
write_csv(city_data)