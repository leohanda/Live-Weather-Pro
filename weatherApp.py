import requests, json

def weather(city):
    response= requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=0c42f7f6b53b244c78a418f4f181282a')
    data = response.json()
    return data

while True:
    city = input("Enter the name of the city: ")
    if city == 'exit':
        break
    data = weather(city)
    if data["cod"]!=200:
        print("The city entered is not identified")
        continue

    else:
        print("Location is ",data['name'],', ',data['sys']['country'],sep='')
        print("Weather of your location is",data["weather"][0]["main"])
        print("Temprature of your location is",data['main']['temp'] - 273.16)
        print("windspeed of your location is",data["wind"]["speed"],'kmph')