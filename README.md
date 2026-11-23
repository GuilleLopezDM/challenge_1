# 🐱🐭 El gato y el ratón — IA con Minimax

> Challenge 1 · Python · Algoritmos de búsqueda adversarial

Simulación en un tablero de 6x6 donde un gato persigue a un ratón. **Los dos personajes están controlados por IA**: en cada turno, cada uno elige su mejor movimiento con el algoritmo **Minimax con poda alfa-beta**.

## 🧠 Cómo funciona

- **Tablero:** matriz con validación de límites y casillas libres.
- **Animales:** clase base `Animal` con las subclases `Gato` y `Raton`. El ratón empieza a la izquierda y el gato a la derecha, en filas aleatorias.
- **Estado:** cada nodo del árbol de búsqueda copia las posiciones y la ronda, y detecta el fin de la partida: gana el gato si atrapa al ratón y gana el ratón si sobrevive 20 rondas.
- **Heurística:** distancia Manhattan entre ambos. El gato busca minimizarla y el ratón, maximizarla.
- **Minimax + alfa-beta:** explora 4 jugadas hacia adelante y poda las ramas que no pueden mejorar el resultado.

## 🚀 Ejecutar

Sin dependencias externas.

```bash
python challenge1.py
```

El tablero se imprime después de cada ronda y al final se anuncia el ganador.

## 📚 Conceptos aplicados

`POO` · `herencia` · `búsqueda adversarial` · `minimax` · `poda alfa-beta` · `heurísticas`
