import tkinter as tk

# BMI hesaplama fonksiyonu
def bmi_hesapla():
    # Giriş değerlerini al
    kilo = float(kilonu_gir.get())
    boy = float(boyu_gir.get())

    # BMI'yi hesapla
    bmi = kilo / (boy ** 2)

    # BMI kategorisini belirle
    if bmi < 18.5:
        kategori = "Zayıf"
    elif bmi < 25:
        kategori = "Normal"
    elif bmi < 30:
        kategori = "Fazla Kilolu"
    else:
        kategori = "Obez"

    # BMI'yi ve kategoriyi göster
    bmi_sonucu.set("BMI: {:.2f} - {} kategorisi".format(bmi, kategori))

# Pencereyi oluştur
pencere = tk.Tk()
pencere.title("BMI Hesaplayıcısı")

# Ekranı düzenle
etiket1 = tk.Label(pencere, text="Kilonuzu girin:")
etiket1.grid(row=0, column=0)

kilonu_gir = tk.Entry(pencere)
kilonu_gir.grid(row=0, column=1)

etiket2 = tk.Label(pencere, text="Boyunuzu girin (metre cinsinden):")
etiket2.grid(row=1, column=0)

boyu_gir = tk.Entry(pencere)
boyu_gir.grid(row=1, column=1)

buton = tk.Button(pencere, text="Hesapla", command=bmi_hesapla)
buton.grid(row=2, column=0)

bmi_sonucu = tk.StringVar()
etiket3 = tk.Label(pencere, textvariable=bmi_sonucu)
etiket3.grid(row=3, column=0)

# Pencereyi göster
pencere.mainloop()