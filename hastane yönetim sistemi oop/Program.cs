using System;
using System.Collections.Generic;

namespace HospitalManagementSystem
{
    public class Doctor
    {
        public int Id;
        public string Name;
        public string Specialty;
        public List<DateTime> AvailableDates = new List<DateTime>();

        public Doctor(int id, string name, string specialty)
        {
            Id = id;
            Name = name;
            Specialty = specialty;

            // Hazır randevu saatleri
            AvailableDates.Add(DateTime.Now.AddDays(1).AddHours(10));
            AvailableDates.Add(DateTime.Now.AddDays(1).AddHours(14));
            AvailableDates.Add(DateTime.Now.AddDays(2).AddHours(11));
        }

        public void Diagnose(Patient patient)
        {
            Console.Write("Tanı giriniz: ");
            string diagnosis = Console.ReadLine();

            Console.Write("İlaçlar (virgülle): ");
            List<string> meds = new List<string>(Console.ReadLine().Split(','));

            patient.MedicalRecords.Add(new Record(patient.Id, diagnosis, meds));
            Console.WriteLine("Tanı ve reçete kaydedildi.");
        }
    }

    public class Patient
    {
        public int Id;
        public string Name;
        public List<Appointment> Appointments = new List<Appointment>();
        public List<Record> MedicalRecords = new List<Record>();

        public Patient(int id, string name)
        {
            Id = id;
            Name = name;
        }

        public void BookAppointment(Doctor doctor, DateTime date)
        {
            Appointments.Add(new Appointment(doctor.Id, Id, date));
            Console.WriteLine($"Randevu alındı → {date}");
        }

        public void ViewRecords()
        {
            if (MedicalRecords.Count == 0)
            {
                Console.WriteLine("Kayıt bulunamadı.");
                return;
            }

            foreach (var r in MedicalRecords)
                Console.WriteLine(r);
        }
    }

    public class Appointment
    {
        static int counter = 1;
        public int Id;
        public int DoctorId;
        public int PatientId;
        public DateTime Date;

        public Appointment(int d, int p, DateTime date)
        {
            Id = counter++;
            DoctorId = d;
            PatientId = p;
            Date = date;
        }
    }

    public class Record
    {
        static int counter = 1;
        public int RecordId;
        public int PatientId;
        public string Diagnosis;
        public List<string> Medications;
        public DateTime Date;

        public Record(int pid, string diag, List<string> meds)
        {
            RecordId = counter++;
            PatientId = pid;
            Diagnosis = diag;
            Medications = meds;
            Date = DateTime.Now;
        }

        public override string ToString()
        {
            return $"[{RecordId}] Tanı: {Diagnosis} | İlaçlar: {string.Join(", ", Medications)} | Tarih: {Date}";
        }
    }

    class Program
    {
        static void Main()
        {
            List<Doctor> doctors = new List<Doctor>()
            {
                new Doctor(1,"Dr. Ahmet","Kardiyoloji"),
                new Doctor(2,"Dr. Ayşe","Nöroloji"),
                new Doctor(3,"Dr. Mehmet","Dahiliye")
            };

            Patient patient = new Patient(1, "Kemal Karatoprak");

            while (true)
            {
                Console.WriteLine("\n1- Randevu Al");
                Console.WriteLine("2- Tanı Koy");
                Console.WriteLine("3- Kayıtları Gör");
                Console.WriteLine("0- Çıkış");
                Console.Write("Seçim: ");

                if (!int.TryParse(Console.ReadLine(), out int secim))
                    continue;

                if (secim == 0) break;

                if (secim == 1)
                {
                    foreach (var d in doctors)
                        Console.WriteLine($"{d.Id} - {d.Name} ({d.Specialty})");

                    Console.Write("Doktor ID: ");
                    if (!int.TryParse(Console.ReadLine(), out int did)) continue;

                    Doctor doc = doctors.Find(x => x.Id == did);
                    if (doc == null) continue;

                    Console.WriteLine("\nMüsait Tarihler:");
                    for (int i = 0; i < doc.AvailableDates.Count; i++)
                        Console.WriteLine($"{i + 1} - {doc.AvailableDates[i]}");

                    Console.Write("Seçim: ");
                    if (!int.TryParse(Console.ReadLine(), out int tsecim)) continue;
                    if (tsecim < 1 || tsecim > doc.AvailableDates.Count) continue;

                    DateTime selectedDate = doc.AvailableDates[tsecim - 1];
                    patient.BookAppointment(doc, selectedDate);
                }

                else if (secim == 2)
                {
                    foreach (var d in doctors)
                        Console.WriteLine($"{d.Id} - {d.Name}");

                    Console.Write("Doktor ID: ");
                    if (!int.TryParse(Console.ReadLine(), out int did)) continue;

                    Doctor doc = doctors.Find(x => x.Id == did);
                    if (doc == null) continue;

                    doc.Diagnose(patient);
                }

                else if (secim == 3)
                {
                    patient.ViewRecords();
                }
            }
        }
    }
}
