# import the module
import python_weather

import asyncio
import os

async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    # fetch a weather forecast from a city
    weather = await client.get('Bergen')
    
    # returns the current day's forecast temperature (int)
    print(weather.temperature)
    
    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      print(daily)
      
      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        print(f' --> {hourly!r}')


if os.name == 'nt':
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(getweather())
  