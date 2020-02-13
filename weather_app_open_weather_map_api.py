from tkinter import *
import requests
import json
from datetime import datetime

window = Tk()

window.title("Weather App")
window.geometry("400x500")


def labels():
    label = Label(window,
                  text="",
                  font=("Helvetica", 20))

    return label


def search():
    try:
        appId = "YOUR_API_KEY"
        zip_code_value = zip_code.get()
        city_value = city.get()
        coords_value = coords.get()
        (label) = labels()

        if not zip_code_value and not city_value and not coords_value:
            label.configure(text="Please enter zip code, city or coordinates")
            label.grid(row=4, column=0, columnspan=2)
            label.after(2000, label.destroy)

        if zip_code_value or city_value or coords_value:
            if zip_code_value:
                url = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip_code_value + "&appid=" + appId
            if city_value:
                url = "https://api.openweathermap.org/data/2.5/weather?q=" + city_value + "&appid=" + appId
            if coords_value:
                [lat, lon] = coords_value.split(",")
                url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon.strip() + "&appid=" + appId

            api_request = requests.get(url)
            api_data = json.loads(api_request.content)

            lon = api_data["coord"]["lon"]
            lat = api_data["coord"]["lat"]
            location = api_data["name"]
            country = api_data["sys"]["country"]
            sunrise = datetime.fromtimestamp(api_data["sys"]["sunrise"])
            sunset = datetime.fromtimestamp(api_data["sys"]["sunset"])
            weather = api_data["weather"][0]["main"]
            weather_des = api_data["weather"][0]["description"]
            wind = api_data["wind"]["speed"]
            temp = api_data["main"]["temp"]
            celsius = float(temp) - 273.15
            humidity = api_data["main"]["humidity"]
            pressure = api_data["main"]["pressure"]

            data = f"City: {location}\n" \
                   f"Country: {country}\n" \
                   f"Longitude: {lon}\n" \
                   f"Latitude: {lat}\n" \
                   f"Weather: {weather} ({weather_des})\n" \
                   f"Temperature: {round(celsius, 2)} °C\n" \
                   f"Wind: {wind} m/s\n" \
                   f"Humidity: {humidity}%\n" \
                   f"Pressure: {pressure} hPa\n" \
                   f"Sunrise: {sunrise}\n" \
                   f"Sunset: {sunset}\n"
            label.configure(text=data)
            label.grid(row=4, column=0, columnspan=2)
            label.after(5000, label.destroy)

            zip_code.delete(0, END)
            city.delete(0, END)
            coords.delete(0, END)
    except Exception as e:
        label.configure(text=f"Error...\n{e}")
        label.grid(row=4, column=1, stick=W+E+N+S)
        label.after(2000, label.destroy)


zip_code_label = Label(window, text="Zip Code")
zip_code_label.grid(row=0, column=0, stick=W+E+N+S)

zip_code = Entry(window)
zip_code.grid(row=0, column=1, stick=W+E+N+S)

city_label = Label(window, text="City Name")
city_label.grid(row=1, column=0, stick=W+E+N+S)

city = Entry(window)
city.grid(row=1, column=1, stick=W+E+N+S)

coords_label = Label(window, text="Coordinates (lat, lon)")
coords_label.grid(row=2, column=0, stick=W+E+N+S)

coords = Entry(window)
coords.grid(row=2, column=1, stick=W+E+N+S)

search_btn = Button(window,
                    text="Search",
                    highlightbackground="#333333",
                    command=search)
search_btn.grid(row=3, column=1, stick=W+E+N+S)

window.mainloop()
