#  Vehicle Management & Efficiency Simulation

Bu proje, Python'da **Soyut Sınıflar (Abstract Classes)**, **Kalıtım (Inheritance)** ve **Kapsülleme (Encapsulation)** gibi ileri düzey Nesne Yönelimli Programlama (OOP) kavramlarını uygulamalı olarak gösteren bir simülasyon sistemidir.

Proje kapsamında bir aracın sürüş mesafesi, yakıt tüketimi ve verimlilik hesaplamaları modellenmiştir.

## OOP Mimari Yapısı

Sistem, sürdürülebilir ve geliştirilebilir bir yapı için hiyerarşik bir sınıf tasarımı kullanır:

### 1. Temel Soyut Sınıf: `Vehicle`
Tüm araç tipleri için ortak bir şablon sunar.
* **Protected Attributes:** `_brand`, `_model`, `_year` nitelikleri ile veri gizliliği sağlanır.
* **Property Decorator:** Marka (`brand`) bilgisine kontrollü erişim sağlar.
* **Abstract Method:** `show_info()` metodu ile alt sınıfların kendi bilgilerini yazdırmasını zorunlu kılar.

### 2. Türetilmiş Sınıf: `Car`
`Vehicle` sınıfından miras alarak otomobillere özgü yetenekler kazanır.
* **Ek Özellikler:** Yakıt türü, toplam kilometre ve harcanan yakıt miktarı.
* **Fonksiyonel Metotlar:**
    * `drive(km)`: Kilometre sayacını günceller.
    * `refuel(liters)`: Yakıt tüketim kaydı tutar.
    * `fuel_efficiency()`: Aracın yakıt verimliliğini (km/l) hesaplar.

---



## Kullanım Örneği

Aşağıdaki kod bloğu, sistemin bir **Tesla Model 3** üzerindeki simülasyonunu temsil eder:

```python
# Nesne oluşturma
tesla = Car("Tesla", "Model 3", 2022, "Electric")

# Simülasyon adımları
tesla.drive(150)        # 150 km sürüş
tesla.refuel(30)       # 30 birim enerji/yakıt tüketimi
tesla.show_info()      # Araç bilgilerini yazdır
print(f"Efficiency: {tesla.fuel_efficiency()} km/l")
