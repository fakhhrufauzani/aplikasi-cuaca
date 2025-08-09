import tkinter as tk
import requests

API_KEY = "ae3724b93ab3441dcaa0f97532349f94"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="❗ Harap masukkan nama kota.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "id"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        result = (
            f"🌍 Kota: {city.title()}\n"
            f"🌡️ Suhu: {data['main']['temp']}°C\n"
            f"💧 Kelembapan: {data['main']['humidity']}%\n"
            f"☁️ Cuaca: {data['weather'][0]['description']}\n"
            f"💨 Angin: {data['wind']['speed']} m/s"
        )
        result_label.config(text=result)
    except:
        result_label.config(text="Kota tidak ditemukan atau jaringan bermasalah.")

# GUI setup
root = tk.Tk()
root.title("Aplikasi Cuaca")
root.geometry("350x250")

title_label = tk.Label(root, text="Cek Cuaca", font=("Arial", 16))
title_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)
city_entry.focus()

check_button = tk.Button(root, text="Cek Cuaca", command=get_weather)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
