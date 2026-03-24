import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

API_KEY = "33589e6974d00a126415f7f89828c688"  # OpenWeatherMap API key

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Hata", "Lütfen bir şehir girin!")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=tr"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        weather_text.set("Şehir bulunamadı! Lütfen şehir adı ve ülke kodunu kontrol edin.\nÖrnek: Istanbul,TR")
        icon_label.configure(image="")
        return

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    icon_code = data["weather"][0]["icon"]
    country = data["sys"]["country"]

    weather_text.set(f"{city}, {country} için hava durumu:\n{desc}\nSıcaklık: {temp}°C")

    # İkonu getir
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_response = requests.get(icon_url)
    img_data = icon_response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((100,100))
    img_tk = ImageTk.PhotoImage(img)

    icon_label.configure(image=img_tk)
    icon_label.image = img_tk

def about():
    messagebox.showinfo(
        "Hakkında",
        "Hava Durumu Uygulaması\n\n"
        "Geliştirici: Mansur Efe Dirikolu\n"
        "Python & Tkinter kullanılarak geliştirilmiştir.\n"
        "API: OpenWeatherMap\n"
        "Windows için EXE sürümü mevcuttur."
    )

# Tkinter arayüzü
window = tk.Tk()
window.title("Hava Durumu ve Şehir Kontrolü")
window.geometry("400x450")

tk.Label(window, text="Şehir girin (örn: Istanbul veya Istanbul,TR):", wraplength=380, justify="center", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(window, text="Hava Durumunu Getir", command=get_weather).pack(pady=10)
tk.Button(window, text="Hakkında", command=about).pack(pady=5)

weather_text = tk.StringVar()
tk.Label(window, textvariable=weather_text, wraplength=380, justify="center", font=("Arial", 12)).pack(pady=15)

icon_label = tk.Label(window)
icon_label.pack()

window.mainloop()
