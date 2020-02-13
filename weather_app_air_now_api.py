from tkinter import *
import requests
import json

window = Tk()

window.title("Python GUI Tkinter")
window.geometry("420x200")


def zipLookup():
    try:
        api_key = "YOUR_API_KEY"
        url = "http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=" + zip_code.get() + \
              "&date=2020-02-11&distance=25&API_KEY=" + api_key
        api_request = requests.get(url)
        api_data = json.loads(api_request.content)
        if not len(api_data):
            label = Label(window,
                          text="No data found!\nPlease try with another zip code.",
                          font=("Helvetica", 20),
                          background="#999999")
            label.grid(row=2, column=1, columnspan=2, stick=W+E+N+S, pady=(20, 0))
            label.after(5000, label.destroy)
            zip_code.delete(0, END)

        i = 0
        for api in api_data:
            city = api["ReportingArea"]
            quality = api["AQI"]
            category = api["Category"]["Name"]

            weather_color = ""
            if category == "Good":
                weather_color = "#00E400"
            elif category == "Moderate":
                weather_color = "#FFFF00"
            elif category == "Unhealthy for Sensitive Groups":
                weather_color = "#FF7E00"
            elif category == "Unhealthy":
                weather_color = "#FF0000"
            elif category == "Very Unhealthy":
                weather_color = "#8f3f97"
            elif category == "Hazardous":
                weather_color = "#7E0023"

            data = city + " Air Quality " + str(quality) + " " + category
            label = Label(window, text=data, font=("Helvetica", 20), background=weather_color)
            label.grid(row=2+int(i), column=0, columnspan=2, stick=W+E+N+S, pady=(20, 0))
            label.after(5000, label.destroy)
            zip_code.delete(0, END)
            i += 1
    except Exception as error:
        label = Label(window,
                      text=f"Error...{error}",
                      font=("Helvetica", 20),
                      background="#999999")
        label.grid(row=2, column=0, columnspan=2, stick=W+E+N+S, pady=(20, 0))


zip_code_label = Label(window, text="Zip Code")
zip_code_label.grid(row=0, column=0, stick=W+E+N+S)

zip_code = Entry(window)
zip_code.grid(row=0, column=1, stick=W+E+N+S)

zip_code_btn = Button(window,
                      text="Zip Code",
                      highlightbackground="#333333",
                      command=zipLookup)
zip_code_btn.grid(row=1, column=1, stick=W+E+N+S)

window.mainloop()
