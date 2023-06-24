import sqlite3
print("Module Imported !")


con = sqlite3.connect('info.db')
print("data file made !")

cursor = con.cursor()
print("cursor connected")

#====================== Table For Teacher/User==============================#

cursor.execute('''create table if not exists user (
unm TEXT,
pas TEXT,
f_nm TEXT,
l_nm TEXT,
E_mail TEXT,
mob INTEGER
)''')
print("table created")

cursor.execute("INSERT INTO user (unm, pas, f_nm, l_nm, E_mail, mob) VALUES(?, ?, ?, ?, ?, ?)",
               (str(ue.get()),
                str(pe.get()),
                str(qe.get()),
                str(ee.get()),
                str(re.get()),
                str(se.get())))
conn.commit()
ue.set("")
pe.set("")
qe.set("")
ee.set("")
re.set("")
se.set("")

#========================Table for Student Record================================#



cursor.close()
conn.close()

