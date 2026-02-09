import random
class Tablero:
    def __init__(self,filas,columnas):
        self.filas = filas
        self.columnas = columnas
        self.tablero=[['*' for i in range(columnas)] for j in range(filas)] #crea una matriz de 0's con el tamaño del tablero
class Raton:
    def __init__(self,tablero):
        self.posicion_x = 0
        self.posicion_y = 0
        self.tablero = tablero

    def mover_raton(self):
        print("Ingrese el movimiento del raton: ")
        while True:
                movimiento = input(
                "1-Para mover a la izquierda\n"
                "2-Para mover a la derecha\n"
                "3-Para mover arriba\n"
                "4-Para mover abajo\n"
                "5-Para salir\n"
                )

                if movimiento == '1':
                    if self.posicion_x > 0:
                        self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del ratón
                        self.posicion_x -= 1
                        self.tablero[self.posicion_y][self.posicion_x] = 'R'  # coloca el ratón en la nueva posición
                        break
                    else:
                        print("No puedes mover a la izquierda, estás en el borde del tablero.")

                elif movimiento == '2':
                    if self.posicion_x < len(self.tablero[0]) - 1:
                        self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del ratón
                        self.posicion_x += 1
                        self.tablero[self.posicion_y][self.posicion_x] = 'R'  # coloca el ratón en la nueva posición
                        break
                    else:
                        print("No puedes mover a la derecha, estás en el borde del tablero.")

                elif movimiento == '3':
                    if self.posicion_y > 0:
                        self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del ratón
                        self.posicion_y -= 1
                        self.tablero[self.posicion_y][self.posicion_x] = 'R'  # coloca el ratón en la nueva posición
                        break
                    else:
                        print("No puedes mover hacia arriba, estás en el borde del tablero.")

                elif movimiento == '4':
                    if self.posicion_y < len(self.tablero) - 1:
                        self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del ratón
                        self.posicion_y += 1
                        self.tablero[self.posicion_y][self.posicion_x] = 'R'  # coloca el ratón en la nueva posición
                        break
                    else:
                        print("No puedes mover hacia abajo, estás en el borde del tablero.")

                elif movimiento == '5':
                    print("Saliendo del juego.")
                    return False

                else:
                    print("Movimiento inválido.")
class Gato:
    def __init__(self,tablero):
        self.posicion_x = len(tablero[0]) - 1
        self.posicion_y = len(tablero) - 1
        self.tablero = tablero
    def mover_gato(self):
        while True:
            movimiento=random.randint(1,4)
            if movimiento == 1 and self.posicion_x > 0:
                self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del gato
                self.posicion_x -= 1
                self.tablero[self.posicion_y][self.posicion_x] = 'G'  # coloca el gato en la nueva posición
                break
            elif movimiento == 2 and self.posicion_x < len(self.tablero[0]) - 1:
                self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del gato
                self.posicion_x += 1
                self.tablero[self.posicion_y][self.posicion_x] = 'G'  # coloca el gato en la nueva posición
                break
            elif movimiento == 3 and self.posicion_y > 0:
                self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del gato
                self.posicion_y -= 1
                self.tablero[self.posicion_y][self.posicion_x] = 'G'  # coloca el gato en la nueva posición
                break
            elif movimiento == 4 and self.posicion_y < len(self.tablero) - 1:
                self.tablero[self.posicion_y][self.posicion_x] = '*'  # borra la posición anterior del gato
                self.posicion_y += 1
                self.tablero[self.posicion_y][self.posicion_x] = 'G'  # coloca el gato en la nueva posición
                break
class Juego:
    def __init__(self,gato,raton,tablero):
        self.gato=gato
        self.raton=raton
        self.tablero=tablero
        self.tablero[self.raton.posicion_y][self.raton.posicion_x]='R'
        self.tablero[self.gato.posicion_y][self.gato.posicion_x]='G'

    def mostrar_juego(self):
        for fila in self.tablero:
            print(' '.join(fila))
    def ejecutar_juego(self):
        self.mostrar_juego()
        while True:
            if self.raton.mover_raton() is False:
                print("El juego ha terminado por el jugador.")
                break
            if self.raton.posicion_x == self.gato.posicion_x and self.raton.posicion_y == self.gato.posicion_y:
                print("¡El gato ha atrapado al ratón! Fin del juego.")
                self.mostrar_juego()
                break
            self.gato.mover_gato()
            if self.raton.posicion_x == self.gato.posicion_x and self.raton.posicion_y == self.gato.posicion_y:
                print("¡El gato ha atrapado al ratón! Fin del juego.")
                self.mostrar_juego()
                break
            self.mostrar_juego()


filas = int(input("Ingrese el número de filas del tablero: "))
columnas = int(input("Ingrese el número de columnas del tablero: "))
tablero1 = Tablero(filas, columnas)
raton1=Raton(tablero1.tablero)
gato1=Gato(tablero1.tablero)
juego1=Juego(gato1,raton1,tablero1.tablero)
juego1.ejecutar_juego()