# Hospital Management System (C# Console App)

Bu proje, C# programlama dili kullanılarak geliştirilmiş, nesne yönelimli programlama (OOP) prensiplerini temel alan bir **Hastane Yönetim Sistemi** simülasyonudur. Sistem; doktor randevuları, hasta kayıtları ve tıbbi tanı süreçlerini yönetmek için tasarlanmıştır.

## Öne Çıkan Özellikler

* **Doktor & Uzmanlık Yönetimi:** Farklı uzmanlık alanlarına sahip doktorların sisteme tanımlanması.
* **Dinamik Randevu Sistemi:** Doktorların müsaitlik durumuna göre tarih ve saat seçimi yapabilme.
* **Tıbbi Kayıt (E-Reçete) Modülü:** Doktorların hastalara tanı koyması ve ilaç reçete etmesi, bu kayıtların hasta geçmişinde saklanması.
* **Geçmiş Görüntüleme:** Hastaya ait tüm tıbbi kayıtların (Tanı, İlaçlar, Tarih) kronolojik olarak listelenmesi.

## Sınıf Yapısı ve Mimari

Proje, sürdürülebilir bir kod yapısı için aşağıdaki sınıflar üzerine inşa edilmiştir:

| Sınıf | Sorumluluk alanı |
| :--- | :--- |
| `Doctor` | Doktor bilgilerini tutar ve `Diagnose` metodu ile hastaya tanı koyar. |
| `Patient` | Hasta bilgilerini, randevularını ve `MedicalRecords` (Tıbbi Kayıtlar) listesini yönetir. |
| `Appointment` | Randevu ID'si, ilgili doktor ve tarih eşleşmesini sağlar. |
| `Record` | Tanı, ilaç listesi ve kayıt tarihini içeren tıbbi dökümleri temsil eder. |


## Kullanım ve Akış

1.  **Randevu Al:** Sistemde kayıtlı doktorlardan (Kardiyoloji, Nöroloji, Dahiliye) birini seçin ve sunulan müsait tarihlerden birine randevu oluşturun.
2.  **Tanı Koy:** Bir doktor seçerek hastaya teşhis koyun ve virgülle ayırarak ilaç listesini girin.
3.  **Kayıtları Gör:** Hastanın o güne kadar aldığı tüm tanıları ve ilaçları listeleyin.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için:

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/kullaniciadiniz/HospitalManagementSystem.git](https://github.com/kullaniciadiniz/HospitalManagementSystem.git)
    ```
2.  Visual Studio veya VS Code ile `Program.cs` dosyasını açın.
3.  `dotnet run` komutu ile uygulamayı başlatın.

## Örnek Çıktı

```text
1- Randevu Al
2- Tanı Koy
3- Kayıtları Gör
0- Çıkış
Seçim: 1

1 - Dr. Ahmet (Kardiyoloji)
2 - Dr. Ayşe (Nöroloji)
...
Randevu alındı → 06.06.2025 14:00:00
