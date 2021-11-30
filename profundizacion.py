import sqlite3
from sqlite3.dbapi2 import connect


def fetch():
 
    conn = sqlite3.connect('heart.db')
    c = conn.cursor()
    c.execute("SELECT pulso FROM sensor")  
    data = c.fetchall()
    #print(data) #imprime todo como lista de tuplas
    lista_salida = []
    
    for x in range(len(data)):
        c.execute("SELECT pulso FROM sensor WHERE id = (?) ",str(10))
        dato = c.fetchone()
        lista_salida.append(dato[0])  
    
    return lista_salida



if __name__ == '__main__':
    print("Ejercicio de profundización")
    print("#######################################################")
    print(fetch())