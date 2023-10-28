import sqlite3
import requests
conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                    fecha TEXT PRIMARY KEY,
                    precio_compra REAL,
                    precio_venta REAL
                )''')

response = requests.get("https://apis.net.pe/api-tipo-cambio/v1/tipo-cambio?fecha=2023")
data = response.json()
for registro in data:
    fecha = registro['fecha']
    precio_compra = registro['compra']
    precio_venta = registro['venta']
    cursor.execute("INSERT INTO sunat_info VALUES (?, ?, ?)", (fecha, precio_compra, precio_venta))
conexion.commit()
cursor.execute("SELECT * FROM sunat_info")
contenido = cursor.fetchall()
for registro in contenido:
    print(registro)
conexion.close()
