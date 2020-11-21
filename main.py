import tkinter as tk
from tkinter import font
import requests
import os
import urllib.request

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def test_function(entry):
    print("This is the entry: ", entry)


def get_weather(city):
    weather_key = '9b898619f0e812139795949f6a6950e3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}
# 9b898619f0e812139795949f6a6950e3

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='picture.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#c8d5fa', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=20, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=9)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Rage Italic', 20), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

day = ['01d.png', '02d.png', '03d.png', '04d.png', '09d.png', '10d.png', '11d.png', '13n.png', '50d.png']
night = ['01n.png', '02n.png', '03n.png', '04n.png', '09n.png', '10n.png', '11n.png', '13n.png', '50n.png']

base_url = 'http://openweathermap.org/img/wn/'
img_dir = './img/'
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# Get the day weather icons
for name in day:
    file_name = img_dir + name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url + name, file_name)

# Repeat the same thing for night weather icons
for name in night:
    file_name = img_dir + name
    if not os.path.exists(file_name):
        urllib.request.urlretrieve(base_url + name, file_name)

root.mainloop()
