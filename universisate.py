import sqlite3 as sql

db=sql.connect("universitate.db")
cur=db.cursor()

def id_studenti():
    cur.execute('''select ID from studenti;''')
    return f"S{(len(cur.fetchall())+1)}"
def id_profesori():
    cur.execute('''select Pro_ID from Profesori;''')
    return f"PROFESORS{(len(cur.fetchall())+1)}"

print("KURSS")
cur.execute('''INSERT or IGNORE into Kursi VALUES(?,?,?,?);''',(input("ID: "),input("Nosaukums: "),input("Kreditpunkti: "),input("Priekšnosacījumi: ")))
db.commit()
print("STUDENTI")
cur.execute('''INSERT or IGNORE into studenti VALUES(?,?,?,?,?);''',(id_studenti(),input("Vards: "),input("Speciealizācija: "),input("Gads: "),input("Kursi: ")))
db.commit()
print("PROFESORI")
cur.execute('''INSERT or IGNORE into Profesori VALUES(?,?,?,?,?);''',(id_profesori(),input("Vards: "),input("Katerda: "),input("Darba vieta: "),input("Kursi: ")))
db.commit()
print("Dati veiksmīgi pievienoti datubāzei.")

cur.execute('''SELECT Specialitate,Absolvesanas_gads FROM studenti;''')
print(cur.fetchall())

cur.execute('''SELECT Nosaukums, Kreditpunkti FROM Kursi;''')
print(cur.fetchall())

cur.execute('''SELECT Darba_kurss,Vards FROM Profesori;''')
print(cur.fetchall())

cur.execute('''SELECT * from studenti;''')
print(cur.fetchall())

cur.execute('''SELECT sum(Kreditpunkti) FROM Kursi;''')
print(cur.fetchall())

cur.execute('''SELECT min(Kreditpunkti) FROM Kursi;''')
print(cur.fetchall())

cur.execute('''SELECT max(Kreditpunkti) FROM Kursi;''')
print(cur.fetchall())

cur.execute('''SELECT avg(Kreditpunkti) FROM Kursi;''')
print(cur.fetchall())

cur.execute('''SELECT count(Kreditpunkti) FROM Kursi;''')
print(cur.fetchall())

db.close()