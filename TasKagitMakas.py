import tkinter as tk
from tkinter import Button, Label, Image, messagebox, PhotoImage
import random

def button_tiklanma(buton_id):
    secenekler = ["Taş", "Kağıt", "Makas"]
    bilgisayar_secimi = random.choice(secenekler)
    
    kullanici_secim = secenekler[buton_id - 1]
    sonuc_resim_yolu=""
    if kullanici_secim == bilgisayar_secimi:
        sonuc_resim_yolu="C:\\Users\\Kemal\\Desktop\\DRAW.png"
    elif (kullanici_secim == "Taş" and bilgisayar_secimi == "Makas") or \
         (kullanici_secim == "Kağıt" and bilgisayar_secimi == "Taş") or \
         (kullanici_secim == "Makas" and bilgisayar_secimi == "Kağıt"):
       
       sonuc_resim_yolu="C:\\Users\\Kemal\\Desktop\\mutlu.png"
    else:
      
       sonuc_resim_yolu="C:\\Users\\Kemal\\Desktop\\üzgünisaret.png"
  
    label_bilgisayar_sonuc.config(text="Bilgisayar Seçimi :"+bilgisayar_secimi)
    label_kullanici_sonuc.config(text="Kullanıcı Seçimi :"+kullanici_secim)
 
    sonuc_resim=PhotoImage(file=sonuc_resim_yolu)
    label_sonuc_resim.config(image=sonuc_resim)
    label_sonuc_resim.image=sonuc_resim


root = tk.Tk()
root.title("Taş Kağıt Makas Oyunu")
root.geometry("400x300")

resim_makas = PhotoImage(file="C:\\Users\\Kemal\\Desktop\\makas.png")
resim_kagit = PhotoImage(file="C:\\Users\\Kemal\\Desktop\\kagit.png")
resim_tas = PhotoImage(file="C:\\Users\\Kemal\\Desktop\\tas.png")

    
label = tk.Label(root, text="Bir Seçim Yapınız.")
label.pack()

label_bilgisayar_sonuc=tk.Label(root,text="")
label_bilgisayar_sonuc.pack()
label_kullanici_sonuc=tk.Label(root,text="")
label_kullanici_sonuc.pack()
button_tas = tk.Button(root, image=resim_tas, command=lambda: button_tiklanma(1))
button_tas.place(x=10, y=40, width=70, height=70)

button_kagit = tk.Button(root, image=resim_kagit, command=lambda: button_tiklanma(2))
button_kagit.place(x=10, y=120, width=70, height=70)

button_makas = tk.Button(root, image=resim_makas, command=lambda: button_tiklanma(3))
button_makas.place(x=10, y=200, width=70, height=70)
label_sonuc_resim=tk.Label(root)
label_sonuc_resim.pack(side="right",padx=50)
root.mainloop()
