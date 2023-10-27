import requests
n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
try:
 
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price_usd = data["bpi"]["USD"]["rate_float"]
    cost_usd = n * price_usd
    print(f"El costo actual de {n} Bitcoins es ${cost_usd:,.4f}")
except requests.RequestException:
    print("Error al consultar la API de CoinDesk")
