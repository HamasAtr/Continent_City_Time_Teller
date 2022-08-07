from datetime import datetime
import pytz

cont = input("Enter a continent name:- ")
city = input("Enter a city name:- ")

cont.capitalize()
city.capitalize()

try:
  tz_PK = pytz.timezone(f'{cont}/{city}') 
  datetime_PK = datetime.now(tz_PK)
  print(f"{city} time:", datetime_PK.strftime("%H:%M:%S"))
except:
  print("Not Availavle or please check your spelling")