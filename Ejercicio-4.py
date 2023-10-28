import requests
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
    with open("bitcoin_prices.txt", "w") as file:
        file.write(f"Precio actual de Bitcoin: {price} USD")
        print("Los datos se han almacenado correctamente en el archivo bitcoin_prices.txt")
except requests.RequestException:
    print("Error al consultar la API de CoinDesk")
