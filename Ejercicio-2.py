import random
from pyfiglet import Figlet
figlet = Figlet()
fuentes_disponibles = figlet.getFonts()
fuente = input("Ingresa el nombre de la fuente (deja en blanco para seleccionar una aleatoria): ")
if not fuente:
    fuente = random.choice(fuentes_disponibles)
texto = input("Ingresa el texto: ")
figlet.setFont(font=fuente)
print(figlet.renderText(texto))
