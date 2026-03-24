import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Fonksiyon: döviz çevirme
def cevir():
    try:
        miktar = float(entry.get())
        from_para = from_combo.get()
        to_para = to_combo.get()

        url = "https://api.exchangerate-api.com/v4/latest/TRY"
        response = requests.get(url)
        data = response.json()

        rates = data["rates"]

        if from_para == "TRY":
            sonuc = miktar * rates[to_para]
        elif to_para == "TRY":
            sonuc = miktar / rates[from_para]
        else:
            sonuc = miktar / rates[from_para] * rates[to_para]

        sonuc_label.config(text=f"Sonuç: {sonuc:.2f} {to_para}")

    except:
        sonuc_label.config(text="Hatalı giriş!")

# Ana pencere
pencere = tk.Tk()
pencere.title("Döviz Çeviri")
pencere.geometry("350x270")

# Başlık
baslik = tk.Label(pencere, text="Döviz Çevirici", font=("Arial",14))
baslik.pack(pady=10)

# Miktar giriş
entry = tk.Entry(pencere)
entry.pack(pady=5)

# Başlangıç para birimi
from_combo = ttk.Combobox(pencere, values=["TRY","USD","EUR","GBP"], state="readonly")
from_combo.set("TRY")
from_combo.pack(pady=5)

# Hedef para birimi
to_combo = ttk.Combobox(pencere, values=["TRY","USD","EUR","GBP"], state="readonly")
to_combo.set("GBP")
to_combo.pack(pady=5)

# Çevir butonu
buton = tk.Button(pencere, text="Çevir", command=cevir)
buton.pack(pady=10)

# Sonuç etiketi
sonuc_label = tk.Label(pencere, text="", font=("Arial",12))
sonuc_label.pack(pady=5)

# Hakkında butonu
hakkinda_btn = tk.Button(
    pencere, 
    text="Hakkında", 
    command=lambda: messagebox.showinfo("Hakkında", "Developed by Mansur Efe Dirikolu\n2026")
)
hakkinda_btn.pack(pady=5)

# Tkinter döngüsü
pencere.mainloop()
