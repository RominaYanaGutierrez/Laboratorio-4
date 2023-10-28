import sqlite3
import requests
conexion = sqlite3.connect('base.db')
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                    fecha TEXT PRIMARY KEY,
                    precio_usd REAL,
                    precio_gbp REAL,
                    precio_eur REAL,
                    precio_pen REAL
                )''')
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()
precio_usd = data["bpi"]["USD"]["rate_float"]
precio_gbp = data["bpi"]["GBP"]["rate_float"]
precio_eur = data["bpi"]["EUR"]["rate_float"]

response_sunat = requests.get("https://apis.net.pe/api-tipo-cambio/v1/tipo-cambio?fecha=2023")
data_sunat = response_sunat.json()
tipo_cambio_pen = data_sunat[0]['venta']
precio_pen = precio_usd * tipo_cambio_pen
precio_eur = precio_usd * precio_eur

fecha_actual = data["time"]["updated"]
cursor.execute("INSERT INTO bitcoin VALUES (?, ?, ?, ?, ?)", (fecha_actual, precio_usd, precio_gbp, precio_eur, precio_pen))
conexion.commit()

cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin")
contenido = cursor.fetchone()
precio_compra_pen = contenido[0] * 10
precio_compra_eur = contenido[1] * 10
print(f"El precio de compra de 10 bitcoins en PEN es: {precio_compra_pen}")
print(f"El precio de compra de 10 bitcoins en EUR es: {precio_compra_eur}")
conexion.close()
