import sqlite3 as sql

def createDB():
    conn = sql.connect("str.db")
    conn.commit()
    conn.close()

def CreateTable():
    conn = sql.connect("str.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE str (
        name text,
        followers integer,
        subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(nombre, followers, subs):
    conn = sql.connect("str.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO str VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("str.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM str"
    cursor.execute(instruccion)
    datos = cursor.fetchall() #se me olvido para que sirve fetchall :u (despues lo cambio)
    conn.commit()
    conn.close()
    print(datos)

def insertRows(streamerlist):
    conn = sql.connect("str.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO str VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamerlist)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("str.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM str ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("str.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM str WHERE subs > 1000 ORDER BY subs DESC" 
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

streamers = [
    ("gcg", 10000, 1321321),
    ("A", 12932, 12912),
    ("adas", 12312, 12312)
]

#readOrdered("subs")
search()