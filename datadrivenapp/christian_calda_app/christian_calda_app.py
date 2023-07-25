import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk



#function to change the weather display type
def fetch_weather():
    city = city_var.get()
    key = "2bc2f4a5e5a44b28b02100722232507"
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=no"

    response = requests.get(url)
    data = response.json()
    location_label.config(text=f"Location: {data['location']['name']}, {data['location']['country']}", font=("Arial", 16, "bold"))
    temp_label.config(text=f"Temperature: {data['current']['temp_c']}°C", font=("Arial", 14))
    condition_label.config(text=f"Condition: {data['current']['condition']['text']}", font=("Arial", 14))
    humidity_label.config(text=f"Humidity: {data['current']['humidity']}%", font=("Arial", 14))
    time_label.config(text=f"Time: {data['location']['localtime']}", font=("Arial", 14))



# Options for cities
cities = ["Dubai", "New York", "Los Angeles", "London", "Paris", "Tokyo", "Sydney" ]

# Tkinter Gui
root = tk.Tk()
root.title("Weather App")
root.geometry("700x550")  # Set initial window size

# Adding image
logo_image = Image.open("weather.png")
logo_photo = ImageTk.PhotoImage(logo_image)

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)


logo_label = tk.Label(frame, image=logo_photo)
logo_label.pack()

title_label = tk.Label(frame, text="Weather App", font=("Arial", 24, "bold"))
title_label.pack(pady=5)

city_label = tk.Label(frame, text="Select City:", font=("Arial", 14))
city_label.pack()

# Create a StringVar to store the selected city
city_var = tk.StringVar(root)
city_var.set(cities[0])  # Set the default city

# Create a combobox to display predefined city options
city_combobox = ttk.Combobox(frame, textvariable=city_var, values=cities, font=("Arial", 12))
city_combobox.pack(pady=10)

get_weather_button = tk.Button(frame, text="Get Weather", command=fetch_weather, font=("Arial", 12, "bold"))
get_weather_button.pack()

location_label = tk.Label(frame, text="", font=("Arial", 16, "bold"))
location_label.pack(pady=5)

temp_label = tk.Label(frame, text="", font=("Arial", 14))
temp_label.pack()

condition_label = tk.Label(frame, text="", font=("Arial", 14))
condition_label.pack()

humidity_label = tk.Label(frame, text="", font=("Arial", 14))
humidity_label.pack()

time_label = tk.Label(frame, text="", font=("Arial", 14))
time_label.pack()

root.mainloop()
