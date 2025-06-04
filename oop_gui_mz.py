import tkinter as tk
from tkinter import Tk,Label,Button,Entry,messagebox #!!!Uzskaitu visas funkcijas, jo pretējā gadījumā messagebox nedarbosies!!!
import csv

#Veidoju klasi Persona un Lietotajs, kas mantos no Personas (backend)
class Persona:
    def __init__(self,vards,uzvards,vecums,epasts): #Inicilizēju klases atribūtus
        self._vards=vards #Privātais atribūts vārds
        self._uzvards=uzvards
        self._vecums=vecums
        self._adrese=epasts
    def saglaba(self): #Funkcija, kas saglabā personas informāciju .csv dokumentā
        with open("personas.csv",mode="a",newline="",encoding="utf-8") as file: #atveru .csv dokumentu pievienošanas režīmā
            writer=csv.writer(file) #Izveidoju csv writer objektu
            writer.writerow([self._vards,self._uzvards,self._vecums,self._adrese]) #Rakstu rindu ar personas informāciju
            messagebox.showinfo("Saglabāts","Persona vai lietotajs tiek saglabāts veiksmīgi .csv dokumentā")

class Lietotajs(Persona):
    def __init__(self,vards,uzvards,vecums,epasts,lietotajvards): #Inicilizēju klases atribūtus, kas mantoti no Personas un pievienoju jaunu atribūtu lietotājvārds
        super().__init__(vards,uzvards,vecums,epasts) #Izsaucu super klases (Persona) __init__ metodi, lai inicializētu mantotos atribūtus
        self.lietotajvards=lietotajvards 
    def izvade(self): #Funkcija, kas izvada lietotāja informāciju
        super().izvade(self) #Mantoto funkciju izvade no Personas klases
    def saglaba(self): #Funkcija, kas saglabā lietotāja informāciju .csv dokumentā
        with open("personas.csv",mode="a",newline="",encoding="utf-8") as file:
            writer=csv.writer(file) #Izveidoju csv writer objektu
            writer.writerow([self._vards, self._uzvards, self._vecums, self._adrese, self.lietotajvards]) #Rakstu rindu ar lietotāja informāciju
            messagebox.showinfo("Saglabāts","Lietotājs tiek saglabāts veiksmīgi .csv dokumentā")

#Veidoju GUI (frontend)
gui=Tk() #Veidoju GUI logu
gui.title("Personas un Lietotāja informācija") #Nosaukums
gui.geometry("300x450") #Loga izmērs
#Ievodu lauki un pogas
vards_prasijums=Label(gui,text="Ievadi vārdu:")
vards_prasijums.pack()
vards_entry=Entry(gui)
vards_entry.pack()
uzvards_prasijums=Label(gui,text="Ievadi uzvārdu:")
uzvards_prasijums.pack()
uzvards_entry=Entry(gui)
uzvards_entry.pack()
vecums_prasijums=Label(gui,text="Ievadi vecumu:")
vecums_prasijums.pack()
vecums_entry=Entry(gui)
vecums_entry.pack()
epasts_prasijums=Label(gui,text="Ievadi e-pastu:")
epasts_prasijums.pack()
epasts_entry=Entry(gui)
epasts_entry.pack()
lietotajvards_prasijums=Label(gui,text="Ievadi lietotājvārdu (ja ir izvelets 'Lietotajs'):")
lietotajvards_prasijums.pack()
lietotajvards_entry=Entry(gui)
lietotajvards_entry.pack()
izveidot_ka_teksts=Label(gui,text="\nIzvēlies, kādu tipu vēlies izveidot:")
izveidot_ka_teksts.pack()
#Radio pogas, lai izvēlētos, vai izveidot Persona vai Lietotājs
izveidot_ka=tk.IntVar()
ka_persona=tk.Radiobutton(gui,text="Persona",variable=izveidot_ka,value=1)
ka_persona.pack()
ka_lietotajs=tk.Radiobutton(gui,text="Lietotājs",variable=izveidot_ka,value=2)
ka_lietotajs.pack()
#Funkcija, kas izvada informāciju uz ekrāna vai saglabā to .csv dokumentā
def pogaekrans(): #Funkcija, kas izvada informāciju uz ekrāna
    vards=vards_entry.get() #Iegūstu ievadīto vārdu
    uzvards=uzvards_entry.get() #Iegūstu ievadīto uzvārdu
    vecums=int(vecums_entry.get()) #Iegūstu ievadīto vecumu
    epasts=epasts_entry.get() #Iegūstu ievadīto e-pastu
    if izveidot_ka.get()==1:  #Persona
        per=Persona(vards,uzvards,vecums,epasts) #Izveidoju Persona objektu
        #parbaudu, vai persona ir pīlngadīga
        if per._vecums<18:
            messagebox.showerror("Nepilngadīgs",f"{per._vards} nav pīlngadīgs(a)") #Ja nav pīlngadīgs, izvada kļūdas ziņojumu
        else: # Ja ir pīlngadīgs, izvada informāciju uz ekrāna
            ekranstxt=Label(gui,text=f"Sauc: {per._vards} {per._uzvards},\nVecums: {per._vecums}, Epasts: {per._adrese}")
            ekranstxt.pack() 
    elif izveidot_ka.get()==2:  #Lietotājs
        lietotajvards=lietotajvards_entry.get() #Iegūstu ievadīto lietotājvārdu
        usr=Lietotajs(vards,uzvards,vecums,epasts,lietotajvards) #Izveidoju Lietotajs objektu
        if usr._vecums<18: #Parbaudu, vai lietotājs ir pīlngadīgs
            messagebox.showerror("Nepilngadīgs",f"{usr._vards} nav pīlngadīgs(a)") #Ja nav pīlngadīgs, izvada kļūdas ziņojumu
        else: # Ja ir pīlngadīgs, izvada informāciju uz ekrāna
             ekranstxt=Label(gui,text=f"Sauc: {usr._vards} {usr._uzvards},\nVecums: {usr._vecums}, Epasts: {usr._adrese},\nLietotājvārds: {usr.lietotajvards}")
             ekranstxt.pack()
def saglabat(): #Funkcija, kas saglabā informāciju .csv dokumentā
    vards=vards_entry.get() #Iegūstu ievadītie dati
    uzvards=uzvards_entry.get()
    vecums=int(vecums_entry.get())
    epasts=epasts_entry.get()
    if izveidot_ka.get()==1:  # Persona
        per=Persona(vards,uzvards,vecums,epasts) #Izveidoju Persona objektu
        per.saglaba() #Saglabāju informāciju .csv dokumentā
    elif izveidot_ka.get()==2:  # Lietotājs
        lietotajvards=lietotajvards_entry.get() #Iegūstu ievadīto lietotājvārdu
        usr=Lietotajs(vards,uzvards,vecums,epasts,lietotajvards) #Izveidoju Lietotajs objektu
        usr.saglaba() #Saglabāju informāciju .csv dokumentā
ekrans=Button(text="Izvādit ekrānu",command=pogaekrans)
datne=Button(text="Saglabāt .csv dokumentā",command=saglabat)
ekrans.pack()
datne.pack()
gui.mainloop()
