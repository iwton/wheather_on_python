from pyowm import OWM

owm = OWM('Your Free Token')  #  here you should insert your TOKEN from the site https://openweathermap.org/api/one-call-api
mgr = owm.weather_manager()

a = str(input('Enter the name of city: '))

observation = mgr.weather_at_place(a)  #  the program recognizes the city in which you want to know the weather
w = observation.weather

b = str(input('What you want to know(choose all, weather or temperature or wind)?: '))  #  asks what you want to know from the weather

temperature = w.temperature('celsius')['temp'] #  recognizes the temperature
wind = w.wind()['speed'] #  know the speed of the wind
status = w.detailed_status  #  displays the status in a more beautiful form

if b == 'temperature':
    print(w.temperature('celsius'))
elif b == 'Weather':
    print(w)
elif b == 'all' or 'All':
    print('In the town ', a, '-',  status + ',' ' temperature', '-', temperature, 'celsius' + ',' ' wind with speed', round(wind), "kilometers per hour(rounded)" )
elif b == 'wind':
    print(round(wind), "kilometers per hour(rounded)")
    
