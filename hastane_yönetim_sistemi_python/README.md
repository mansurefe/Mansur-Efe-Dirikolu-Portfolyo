# Hospital Appointment & Patient Record System

Bu proje, Python programlama dili kullanılarak geliştirilmiş, temel Nesne Yönelimli Programlama (OOP) prensiplerini sergileyen bir **Hastane Randevu ve Kayıt Yönetim Sistemi** simülasyonudur. 

Sistem; doktorların çalışma saatlerini yönetmek, hastaların randevu almasını sağlamak ve tıbbi kayıtları (tanı/reçete) dijital olarak tutmak için tasarlanmıştır.

## Temel Özellikler

* **Dinamik Doktor Yönetimi:** Doktorların uzmanlık alanlarına göre tanımlanması ve müsaitlik durumlarının takibi.
* **Otomatik Slot Oluşturma:** `add_availabilities_for_range` fonksiyonu ile belirli tarih ve saat aralıkları için toplu randevu saatleri oluşturma.
* **Akıllı Randevu Sistemi:** * Müsait saatlerin listelenmesi ve seçilmesi.
    * Randevu alındığında ilgili saatin doktorun takviminden otomatik olarak düşülmesi.
    * Randevu durumunun (Status) takibi.
* **Tıbbi Kayıt Sistemi:** Hastalar için tanı ve ilaç bilgilerini içeren, tarih damgalı tıbbi geçmiş oluşturma.

## Teknik Yapı

Proje aşağıdaki sınıflar (classes) üzerine inşa edilmiştir:

| Sınıf | Açıklama |
| :--- | :--- |
| `Doctor` | Doktor bilgilerini ve uygunluk (availability) listesini yönetir. |
| `Patient` | Hasta bilgilerini, randevularını ve `Record` nesnelerini saklar. |
| `Appointment` | Randevu ID, doktor/hasta eşleşmesi ve durum bilgisini tutar. |
| `Record` | Hastanın geçmiş tanılarını ve reçetelenmiş ilaçlarını yönetir. |

## Başlangıç

### Gereksinimler
* Python 3.x sürümü.

### Çalıştırma
Projeyi yerel makinenizde çalıştırmak için terminale şu komutu yazın:
```bash
python program.py
