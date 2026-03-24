import tkinter as tk
from tkinter import messagebox
import requests

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()

    if data["type"] == "single":
        joke_text.set(data["joke"])
    else:
        joke_text.set(data["setup"] + "\n\n" + data["delivery"])

def about():
    messagebox.showinfo(
        "Hakkında",
        "Rastgele Şaka Uygulaması\n\n"
        "Geliştirici: Mansur Efe Dirikolu\n"
        "Python & Tkinter kullanılarak geliştirilmiştir.\n"
        "API: JokeAPI"
    )

window = tk.Tk()
window.title("Rastgele Şaka Uygulaması")
window.geometry("400x320")

title = tk.Label(window, text="Rastgele Şaka", font=("Arial",16))
title.pack(pady=10)

joke_text = tk.StringVar()

joke_label = tk.Label(window, textvariable=joke_text, wraplength=350, justify="center")
joke_label.pack(pady=20)

button = tk.Button(window, text="Yeni Şaka Getir", command=get_joke)
button.pack(pady=10)

about_button = tk.Button(window, text="Hakkında", command=about)
about_button.pack(pady=5)

window.mainloop()