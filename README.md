# Separación de Variables vs Método de Euler

## Problema
Se resuelve la ecuación diferencial dy/dt = 2y con y(0) = 1
en el intervalo t ∈ [0,1] con paso h = 0.2.

## Solución Analítica
Separando variables e integrando se obtiene: y(t) = e^(2t)

## Método de Euler
Se aproxima la solución usando la fórmula:
y(i+1) = y(i) + h * f(t, y)

## Resultados
El código imprime una tabla comparando ambas soluciones
y genera una gráfica mostrando la diferencia entre ellas.

## Requisitos
pip install numpy matplotlib

## Ejecución
python solucion.py
