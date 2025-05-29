from tkinter import Tk,Label,Button,messagebox
import csv

#Veidoju klasi Persona un Lietotajs, kas mantos no Personas (backend)
class Persona:
    def __init__(self,vards,uzvards,vecums,epasts):
        self._vards=vards
        self._uzvards=uzvards
        self._vecums=vecums
        self._adrese=epasts
    def izvade(self):
        if self._vecums<18:
            return f"Persona nav pilngadīgs"
        else:
            return f"Sauc: {self._vards} {self._uzvards},\nVecums: {self._vecums}, Epasts: {self._adrese}"
    def saglaba(self):
        if self._vecums<18:
            messagebox.showerror("Nepilngadīgs","Persona nav pilngadīga!")
        else:
            with open("personas.csv", mode="a",newline="",encoding="utf-8") as file:
                writer=csv.writer(file)
                writer.writerow([self._vards,self._uzvards,self._vecums,self._adrese])

class Lietotajs(Persona):
    def __init__(self,vards,uzvards,vecums,epasts,lietotajvards):
        super().__init__(vards,uzvards,vecums,epasts)
        self.lietotajvards=lietotajvards
    def izvade(self):
        if self._vecums<18:
            return f"Persona nav pilngadīgs"
        else:
            return super().izvade()+f",\nLietotajvards: {self.lietotajvards}"
    def saglaba(self):
        if self._vecums<18:
            messagebox.showerror("Nepilngadīgs","Lietotajs nav pilngadīgs!")
        else:
            with open("lietotaji.csv", mode="a",newline="",encoding="utf-8") as file:
                writer=csv.writer(file)
                writer.writerow([self._vards,self._uzvards,self._vecums,self._adrese,self.lietotajvards])

#Veidoju 
pers=Persona(vards="Jānis",uzvards="Bērziņš",vecums=int(input("Ievādi persona vēcumu: ")),epasts="janisberzins@epasts.lv")
usr=Lietotajs(vards="Mihails",uzvards="Žilins",vecums=int(input(f"Ievādi lietotaja vēcumu: ")),epasts="mzilin729@gmail.com",lietotajvards="Maikus")

#Veidoju GUI (frontend)
gui=Tk()
gui.title("Saglabāt ka...")
gui.geometry("400x175")
izvade=Label(gui,text=pers.izvade(),font=("segou ui",12,"italic"))
izvade2=Label(gui,text=usr.izvade(),font=("consolas", 12,))
def pogaekrans():
    izvade.pack()
    izvade2.pack()
def saglabat():
    pers.saglaba()
    usr.saglaba()
    messagebox.showinfo("Tiek saglabāts vieksmīgī","Faili personas.csv un lietotaji.csv\ntiek saglabāti!")
ekrans=Button(text="Izvādit ekrānu",command=pogaekrans)
datne=Button(text="Saglabāt .csv dokumentā",command=saglabat)
ekrans.pack()
datne.pack()
gui.mainloop()
