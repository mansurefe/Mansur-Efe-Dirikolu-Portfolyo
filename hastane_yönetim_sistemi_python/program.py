from datetime import datetime

class Doctor:
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty
        self.availability = []

    def add_availability(self, date_time_str):
        dt = self.parse_datetime(date_time_str)
        if dt:
            self.availability.append(dt)
        else:
            print(f"Hatalı tarih formatı: {date_time_str}")

    @staticmethod
    def parse_datetime(date_time_str):
        try:
            return datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
        except ValueError:
            return None

class Patient:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        self.appointments = []
        self.records = []

    def book_appointment(self, doctor, date_time):
        for available_slot in doctor.availability:
            if (available_slot.year == date_time.year and
                available_slot.month == date_time.month and
                available_slot.day == date_time.day and
                available_slot.hour == date_time.hour and
                available_slot.minute == date_time.minute):
                appointment = Appointment(len(self.appointments) + 1, doctor.id, self.id, available_slot)
                self.appointments.append(appointment)
                doctor.availability.remove(available_slot)
                return appointment
        return None

class Appointment:
    def __init__(self, id, doctor_id, patient_id, date_time):
        self.id = id
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date_time = date_time
        self.status = "Planned"

    def confirm(self):
        self.status = "Confirmed"

class Record:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.entries = []

    def add_entry(self, diagnosis, medications):
        entry = {
            "diagnosis": diagnosis,
            "medications": medications,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        self.entries.append(entry)

    def view_entries(self):
        if not self.entries:
            print("Kayıt bulunamadı.")
        else:
            print(f"\n📋 {self.patient_id} nolu hasta kayıtları:")
            for i, entry in enumerate(self.entries, 1):
                print(f"\nKayıt {i}:")
                print(f"  Tarih: {entry['date']}")
                print(f"  Tanı: {entry['diagnosis']}")
                print(f"  İlaçlar: {', '.join(entry['medications'])}")

def add_availabilities_for_range(doctor, date_str, start_hour, end_hour):
    for hour in range(start_hour, end_hour + 1):
        dt_str = f"{date_str} {hour:02d}:00"
        doctor.add_availability(dt_str)


doctor1 = Doctor(1, "Dr. Ahmet", "Kardiyoloji")
doctor2 = Doctor(2, "Dr. Ayşe", "Dermatoloji")
doctor3 = Doctor(3, "Dr. Mehmet", "Ortopedi")

for doctor in [doctor1, doctor2, doctor3]:
    add_availabilities_for_range(doctor, "2025-06-05", 10, 18)

doctors = [doctor1, doctor2, doctor3]

patient = Patient(101, "Mehmet Yılmaz", 45)
record = Record(patient.id)
patient.records.append(record)

while True:
    print("\n1. Randevu Al")
    print("2. Reçete Yaz")
    print("3. Kayıtları Görüntüle")
    print("4. Çıkış")
    choice = input("Seçiminiz: ")

    if choice == '1':
        print("\nDoktorlar:")
        for doc in doctors:
            print(f"{doc.id}. {doc.name} ({doc.specialty})")
        doc_choice = input("Randevu almak istediğiniz doktorun numarasını girin: ")

        selected_doctor = next((d for d in doctors if str(d.id) == doc_choice), None)
        if not selected_doctor:
            print("Geçersiz doktor seçimi!")
            continue

        print(f"{selected_doctor.name} için müsait saatler:")
        for i, slot in enumerate(selected_doctor.availability, 1):
            print(f"{i}. {slot.strftime('%Y-%m-%d %H:%M')}")

        slot_num = input("Randevu almak istediğiniz saat numarasını seçin: ")
        if not slot_num.isdigit() or int(slot_num) < 1 or int(slot_num) > len(selected_doctor.availability):
            print("Geçersiz saat numarası!")
            continue

        chosen_slot = selected_doctor.availability[int(slot_num) - 1]

        appointment = patient.book_appointment(selected_doctor, chosen_slot)
        if appointment:
            appointment.confirm()
            print(f"Randevu alındı: {chosen_slot.strftime('%Y-%m-%d %H:%M')} - Doktor: {selected_doctor.name}")
        else:
            print("Bu saat müsait değil!")

    elif choice == '2':
        diagnosis = input("Tanı: ")
        meds = input("İlaçlar (virgülle ayırın): ").split(',')
        meds = [m.strip() for m in meds]
        record.add_entry(diagnosis, meds)
        print("Kayıt eklendi.")

    elif choice == '3':
        record.view_entries()

    elif choice == '4':
        print("Programdan çıkılıyor.")
        break

    else:
        print("Geçersiz seçim!")
