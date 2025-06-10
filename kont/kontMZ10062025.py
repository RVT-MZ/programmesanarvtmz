#importeju nepieciešamas bibliotekas
import sqlite3 as sql
import csv
#savienojas ar datubazi
db=sql.connect("uznemums.db") #savienojas ar datubazī
cur=db.cursor() #savienojas cursoru ar datubazī
#Automatīska ID ievietošana
def darb_auto_id():
    cur.execute('''SELECT * FROM Darbinieki;''') #izpīldoju komandu sql
    return f"D{len(cur.fetchall())+1}" #izvada ID

def nod_auto_id():
    cur.execute('''SELECT * FROM Nodala;''') #izpīldoju komandu sql
    return f"N{len(cur.fetchall())+1}" #izvada ID

def proj_auto_id():
    cur.execute('''SELECT * FROM Projekti;''') #izpīldoju komandu sql
    return f"P{len(cur.fetchall())+1}" #izvada ID

print("IEVĀDE") #Lai lietotajam būt saprotamāk
print("DARBINIEKI")
#cur.execute=ievāde komandu
#db.commit()=izveidot komandu
cur.execute('''INSERT or IGNORE INTO Darbinieki VALUES(?,?,?,?);''',(print(darb_auto_id()),input("Vards: "),input("Amats: "),input("Alga: ")))
db.commit()
print("NODAĻA")
cur.execute('''INSERT or IGNORE INTO Nodala VALUES(?,?,?);''',(print(nod_auto_id()),input("Nodaļa nosaukums: "),input("Vaditajs: ")))
db.commit()
print("PROJEKTI")
cur.execute('''INSERT or IGNORE INTO Projekti VALUES(?,?,?,?,?,?);''',(print(proj_auto_id()),input("Nosaukums: "),input("Budžets: "),input("Termiņš(DD.MM.YYYY): "),input("Darbinieka ID: "),input("Nodaļa ID: ")))
db.commit()

#2. [...] atlasīt nepieciešamo informāciju

cur.execute('''SELECT Vards,Alga FROM Darbinieki;''') #izpīldoju komandu sql
print(cur.fetchall())#izvade izdaritu komandu

cur.execute('''SELECT Nod_nosaukums,Vaditajs FROM Nodala;''') #izpīldoju komandu sql
print(cur.fetchall())#izvade izdaritu komandu

cur.execute('''SELECT Proj_nosaukums,Budzets FROM Projekti;''') #izpīldoju komandu sql
print(cur.fetchall())#izvade izdaritu komandu

#3. [...] saglabā to csv datnē [...]

with open("tehno_vards.csv","w") as table: #savienojas ar tabulu
    w=csv.writer(table) #izveidoju mainīgu kā ierakstītajs
    cur.execute('''SELECT count(Budzets) FROM Projekti;''') #izpīldoju komandu sql
    count=(cur.fetchall()) #ierākstu atbīlde mainigā
    print(count) #izvādu uz ekranu
    w.writerow(count) #ierakstu atbīlde tabulā
    cur.execute('''SELECT min(Budzets) FROM Projekti;''') #izpīldoju komandu sql
    min=(cur.fetchall()) #ierākstu atbīlde mainigā
    print(min) #izvādu uz ekranu
    w.writerow(min) #ierakstu atbīlde tabulā
    cur.execute('''SELECT max(Budzets) FROM Projekti;''') #izpīldoju komandu sql
    max=(cur.fetchall()) #ierākstu atbīlde mainigā
    print(max) #izvādu uz ekranu
    w.writerow(max) #ierakstu atbīlde tabulā
    cur.execute('''SELECT avg(Budzets) FROM Projekti;''') #izpīldoju komandu sql
    avg=(cur.fetchall()) #ierākstu atbīlde mainigā
    print(avg) #izvādu uz ekranu
    w.writerow(avg) #ierakstu atbīlde tabulā
    cur.execute('''SELECT sum(Budzets) FROM Projekti;''') #izpīldoju komandu sql
    sum=(cur.fetchall()) #ierākstu atbīlde mainigā
    print(sum) #izvādu uz ekranu
    w.writerow(sum) #ierakstu atbīlde tabulā
    table.close() #aizvēru tabulu

db.close() #izvēru datubazi
