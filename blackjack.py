import random

# Crear una baraja
baraja = [
    'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
    'As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
]

# Función para calcular el valor de una mano
def calcular_valor(mano):
    valor = 0
    ases = 0

    for carta in mano:
        if carta == 'As':
            valor += 11
            ases += 1
        elif carta in ['J', 'Q', 'K']:
            valor += 10
        else:
            valor += int(carta)

    # Ajustar el valor si hay ases y se supera 21
    while valor > 21 and ases > 0:
        valor -= 10
        ases -= 1

    return valor

# Función para mostrar las cartas de una mano
def mostrar_cartas(mano):
    for carta in mano:
        print(carta)

# Juego principal
print("¡Bienvenido a Blackjack!")

while True:
    # Barajar las cartas
    random.shuffle(baraja)

    # Inicializar las manos del jugador y la computadora
    jugador = []
    computadora = []

    # Repartir las dos primeras cartas
    jugador.append(baraja.pop())
    computadora.append(baraja.pop())
    jugador.append(baraja.pop())
    computadora.append(baraja.pop())

    print("Tu mano:")
    mostrar_cartas(jugador)
    print("Valor de tu mano:", calcular_valor(jugador))
    print("Carta visible de la computadora:", computadora[0])

    # Turno del jugador
    while True:
        accion = input("¿Qué deseas hacer? (Pedir/Pasar): ").lower()

        if accion == "pedir":
            jugador.append(baraja.pop())
            print("Tu mano:")
            mostrar_cartas(jugador)
            print("Valor de tu mano:", calcular_valor(jugador))

            if calcular_valor(jugador) > 21:
                print("Te has pasado de 21. ¡Perdiste!")
                break
        elif accion == "pasar":
            break
        else:
            print("Acción no válida. Por favor, elige 'Pedir' o 'Pasar'.")

    if calcular_valor(jugador) > 21:
        continue

    # Turno de la computadora
    print("Mano de la computadora:")
    mostrar_cartas(computadora)
    print("Valor de la mano de la computadora:", calcular_valor(computadora))

    while calcular_valor(computadora) < 17:
        computadora.append(baraja.pop())
        print("La computadora pide una carta.")
        print("Mano de la computadora:")
        mostrar_cartas(computadora)
        print("Valor de la mano de la computadora:", calcular_valor(computadora))

    # Determinar el resultado
    valor_jugador = calcular_valor(jugador)
    valor_computadora = calcular_valor(computadora)

    print("Tu mano final:")
    mostrar_cartas(jugador)
    print("Valor de tu mano:", valor_jugador)

    print("Mano final de la computadora:")
    mostrar_cartas(computadora)
    print("Valor de la mano de la computadora:", valor_computadora)

    if valor_jugador > 21:
        print("¡Perdiste!")
    elif valor_computadora > 21:
        print("¡Ganaste!")
    elif valor_jugador > valor_computadora:
        print("¡Ganaste!")
    elif valor_jugador < valor_computadora:
        print("¡Perdiste!")
    else:
        print("¡Empate!")

    jugar_nuevamente = input("¿Deseas jugar nuevamente? (Sí/No): ").lower()
    if jugar_nuevamente != "sí":
        break

print("¡Gracias por jugar!")
