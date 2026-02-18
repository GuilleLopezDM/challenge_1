#Se importa las librerias random y math
import random
import math

#se crea la clase tablero
class Tablero:
    vacio="*"
    def __init__(self,filas,columnas): #metodo constructor
        self.filas = filas
        self.columnas = columnas
        self.tablero=[[self.vacio for i in range(columnas)] for j in range(filas)]
    def dentro(self,x,y):
        return 0<=x<self.columnas and 0<=y<self.filas
    def caminable(self,x,y): 
        return  self.dentro(x,y) and self.tablero[y][x]==self.vacio
    

class Animal:
    def __init__(self,tablero,posicion_x,posicion_y):
         self.tablero=tablero
         self.posicion_x=posicion_x
         self.posicion_y=posicion_y
    def mover_animal(self,dx,dy):
        nx,ny=self.posicion_x+dx,self.posicion_y+dy
        if (dx==0 and dy==0):
            return False
        elif self.tablero.caminable(nx,ny):
            self.posicion_x,self.posicion_y=nx,ny
            return True
        else:
            return False


class Raton(Animal):
    simbolo="R"
    def __init__(self,tablero):
        super().__init__(tablero,1,random.randint(0,tablero.filas-1))


class Gato(Animal):
    simbolo="G"
    def __init__(self,tablero):
        super().__init__(tablero,tablero.columnas-1,random.randint(0,tablero.filas-1))

class Estado:
    def __init__(self,rx,ry,gx,gy,rondas):
        self.rx=rx
        self.ry=ry
        self.gx=gx
        self.gy=gy
        self.rondas=rondas
    def copia(self):
        return Estado(self.rx,self.ry,self.gx,self.gy,self.rondas)
    def termina_estado(self):
        if (self.rx==self.gx and self.ry==self.gy):
            return "GATO"
        elif self.rondas>=20:
            return "RATON"
        else:
            return None
class Juego:
    movs=[(1,0),(0,1),(-1,0),(0,-1)]
    def __init__(self,tablero,raton,gato):
        self.tablero=tablero
        self.raton=raton
        self.gato=gato

    def heuristica(self,estado):
        manhattan=abs(estado.rx - estado.gx) + abs(estado.ry - estado.gy)
        return manhattan
    
    def mostrar_juego(self):
        aux=[fila.copy() for fila in self.tablero.tablero]
        aux[self.raton.posicion_y][self.raton.posicion_x]=self.raton.simbolo
        aux[self.gato.posicion_y][self.gato.posicion_x]=self.gato.simbolo
        for fila in aux:
            print(' '.join(fila))
        print("\n")

    def movimientos_validos(self,x,y):
        validos=[]
        for (dx,dy) in self.movs:
            nx,ny=x+dx,y+dy
            if self.tablero.caminable(nx,ny):
                validos.append((dx,dy))
        return validos
    
        
    def estado_actual(self,ronda_actual):
        rx=self.raton.posicion_x
        ry=self.raton.posicion_y
        gx=self.gato.posicion_x
        gy=self.gato.posicion_y
        return Estado(rx,ry,gx,gy,ronda_actual)
    def siguiente_estado(self,estado,turno,mov):
        dx=mov[0]
        dy=mov[1]
        nuevo_estado=estado.copia()
        if turno=="R":
            nuevo_estado.rx=estado.rx+dx
            nuevo_estado.ry=estado.ry+dy
        elif turno=="G":
            nuevo_estado.gx=estado.gx+dx
            nuevo_estado.gy=estado.gy+dy
            nuevo_estado.rondas=estado.rondas+1
        return nuevo_estado
    def evaluar(self,estado):
        resultado=estado.termina_estado()
        if resultado!=None:
            if resultado=="RATON":
                return +100000
            elif resultado=="GATO":
                return -100000
        return self.heuristica(estado)
    def minimax(self,estado,depth,turno,alfa,beta):
        if depth==0:
            return self.evaluar(estado)
        if estado.termina_estado()!=None:
            return self.evaluar(estado)
        elif turno=="R":
            mejor=-math.inf
            movs=self.movimientos_validos(estado.rx,estado.ry)
            if movs==[]:
                return self.evaluar(estado)
            for movimiento in movs:
                hijo=self.siguiente_estado(estado,"R",movimiento)
                score=self.minimax(hijo,depth-1,"G",alfa,beta)
                mejor=max(mejor,score)
                alfa=max(alfa,mejor)
                if beta<=alfa:
                    break
            return mejor
        elif turno=="G":
            mejor=math.inf
            movs=self.movimientos_validos(estado.gx,estado.gy)
            if movs==[]:
                return self.evaluar(estado)
            for movimiento in movs:
                hijo=self.siguiente_estado(estado,"G",movimiento)
                score=self.minimax(hijo,depth-1,"R",alfa,beta)
                mejor=min(mejor,score)
                beta=min(beta,mejor)
                if beta<=alfa:
                    break
            return mejor
    def mejor_movimiento(self,estado,turno,depth):
        alfa,beta=-math.inf,math.inf
        if turno=="R":
            movs=self.movimientos_validos(estado.rx,estado.ry)
            if movs==[]:
                return None
            mejor_puntaje=-math.inf
            mejor_mov=movs[0]
            for movimiento in movs:
                hijo=self.siguiente_estado(estado,"R",movimiento)
                score=self.minimax(hijo,depth-1,"G",alfa,beta)
                if score>mejor_puntaje:
                    mejor_puntaje=score
                    mejor_mov=movimiento
                alfa=max(alfa,mejor_puntaje)
                if beta<=alfa:
                    break
            return mejor_mov
        elif turno=="G":
            movs=self.movimientos_validos(estado.gx,estado.gy)
            if movs==[]:
                return None
            mejor_puntaje=+math.inf
            mejor_mov=movs[0]
            for movimiento in movs:
                hijo=self.siguiente_estado(estado,"G",movimiento)
                score=self.minimax(hijo,depth-1,"R",alfa,beta)
                if score<mejor_puntaje:
                    mejor_puntaje=score
                    mejor_mov=movimiento
                beta=min(beta,mejor_puntaje)
                if beta<=alfa:
                    break
            return mejor_mov

    def ejecutar_juego(self):
        self.mostrar_juego()
        cant_rondas=0
        depth=4
        while True:
            estado_raton=self.estado_actual(cant_rondas)
            mov=self.mejor_movimiento(estado_raton,"R",depth)
            if mov!=None:
                self.raton.mover_animal(mov[0],mov[1])
            estado_raton=self.estado_actual(cant_rondas)
            resultado=estado_raton.termina_estado()
            if resultado!=None:
                print(f"El ganador es el: {resultado}")
                break
            estado_gato=self.estado_actual(cant_rondas)
            mov=self.mejor_movimiento(estado_gato,"G",depth)
            if mov!=None:
                self.gato.mover_animal(mov[0],mov[1])
            cant_rondas=cant_rondas+1
            estado_gato=self.estado_actual(cant_rondas)
            resultado=estado_gato.termina_estado()
            if resultado!=None:
                print(f"El ganador es el: {resultado}")
                break
            self.mostrar_juego()

if __name__ == "__main__":
    tablero1 = Tablero(6, 6)
    raton1 = Raton(tablero1)
    gato1 = Gato(tablero1)
    juego1 = Juego(tablero1, raton1, gato1)
    juego1.ejecutar_juego()