import random
import tkinter
import os
sayilar = "0123456789"
kucukHarf = "abcdefghijklmnopqrstuvwxyz"
buyukHarf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sembol = "~`!@#$%^&*()_-+={[}]|\:;'<,>.?/"
sifrem =""
class Creator:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Şifre Oluşturucu")
        self.screen_width = self.mainWindow.winfo_screenwidth()
        self.screen_height = self.mainWindow.winfo_screenheight()
        self.mainWindow.geometry(f"400x450+{(self.screen_width//2)-200}+{(self.screen_height//2)-300}")
        self.mainWindow.resizable(width=False,height=False)
        self.top = tkinter.Frame(self.mainWindow)
        self.mid = tkinter.Frame(self.mainWindow)
        self.bottom = tkinter.Frame(self.mainWindow)
        self.sayiVar = tkinter.IntVar()
        self.kucukVar = tkinter.IntVar()
        self.buyukVar = tkinter.IntVar()
        self.sembolVar = tkinter.IntVar()
        self.sayiVar.set(0)
        self.kucukVar.set(0)
        self.buyukVar.set(0)
        self.sembolVar.set(0)
        self.sayiCheck = tkinter.Checkbutton(self.top, text="Sayı",variable = self.sayiVar , command= self.secilebilir)
        self.sayiCheck.pack()
        self.sayi = tkinter.Scale(self.top,orient="horizontal",from_=0, to=10,state="disabled")
        self.sayi.pack()
        self.kucukCheck = tkinter.Checkbutton(self.top, text="Küçük Harf",variable = self.kucukVar , command= self.secilebilir)
        self.kucukCheck.pack()
        self.kucukHarf = tkinter.Scale(self.top,orient="horizontal",from_=0, to=10,state="disabled")
        self.kucukHarf.pack()
        self.buyukCheck = tkinter.Checkbutton(self.top, text="Büyük Harf",variable = self.buyukVar , command= self.secilebilir)
        self.buyukCheck.pack()
        self.buyukHarf = tkinter.Scale(self.top,orient="horizontal",from_=0, to=10,state="disabled")
        self.buyukHarf.pack()
        self.sembolCheck = tkinter.Checkbutton(self.top, text="Semol",variable = self.sembolVar , command= self.secilebilir)
        self.sembolCheck.pack()
        self.sembolS = tkinter.Scale(self.top,orient="horizontal",from_=0, to=10,state="disabled")
        self.sembolS.pack()
        self.olusturButon = tkinter.Button(self.mid,text="Şifre Oluştur",command= self.olusturma)
        self.olusturButon.pack()
        self.sifreVar = tkinter.StringVar()
        self.sifreLabel = tkinter.Label(self.bottom,textvariable=self.sifreVar,font=("Arial",25))
        self.sifreLabel.pack()
        self.sifreAd = tkinter.Label(self.bottom,text="Şifrenize İsim Koyun")
        self.sifreAd.pack()
        self.sifreIsim = tkinter.Entry(self.bottom)
        self.sifreIsim.pack()
        self.kayitButon = tkinter.Button(self.bottom,text="Kaydet",command=self.kaydet)
        self.kayitButon.pack()
        self.top.pack()
        self.mid.pack()
        self.bottom.pack()
        tkinter.mainloop()
    def secilebilir(self):
        if self.sayiVar.get():
            self.sayi.config(state="active")
        else:
            self.sayi.set(0)
            self.sayi.config(state="disabled")
            self.mainWindow.update_idletasks()
        if self.kucukVar.get():
            self.kucukHarf.config(state="active")
        else:
            self.kucukHarf.set(0)
            self.kucukHarf.config(state="disabled")
            self.mainWindow.update_idletasks()
        if self.buyukVar.get():
            self.buyukHarf.config(state="active")
        else:
            self.buyukHarf.set(0)
            self.buyukHarf.config(state="disabled")
            self.mainWindow.update_idletasks()
        if self.sembolVar.get():
            self.sembolS.config(state="active")
        else:
            self.sembolS.set(0)
            self.sembolS.config(state="disabled")
            self.mainWindow.update_idletasks()
    def olusturma(self):
        global sifrem
        sifrem = ''
        if self.sayiVar.get():
            for i in range(0,self.sayi.get()):
                karakter = random.choice(sayilar)
                sifrem = sifrem + karakter
        if self.kucukVar.get():
            for j in range(0,self.kucukHarf.get()):
                karakter = random.choice(kucukHarf)
                sifrem = sifrem + karakter
        if self.buyukVar.get():
            for k in range(0,self.buyukHarf.get()):
                karakter = random.choice(buyukHarf)
                sifrem = sifrem + karakter
        if self.sembolVar.get():
            for l in range(0,self.sembolS.get()):
                karakter = random.choice(sembol)
                sifrem = sifrem + karakter
        sifreListe = list(sifrem)
        random.shuffle(sifreListe)
        sifrem = ''.join(sifreListe)
        self.sifreVar.set(sifrem)
    def kaydet(self):
        satir = self.sifreIsim.get() + "=" + self.sifreVar.get() + '\n'
        dizin = os.getcwd()
        if open(f'{dizin}/sifrelerim.txt','a'):
            dosya = open(f'{dizin}/sifrelerim.txt','a')
            dosya.write(satir)
        else:
            dosya = open(f'{dizin}/sifrelerim.txt','w')
            dosya.write(satir)
        dosya.close()
if __name__ == '__main__':
    Creator()
