import numpy as np
import matplotlib.pyplot as plt

# --- Solución Analítica ---
t_exacto = np.linspace(0, 1, 100)
y_exacto = np.exp(2 * t_exacto)

# --- Método de Euler ---
h = 0.2
t_euler = np.arange(0, 1 + h, h)
y_euler = np.zeros(len(t_euler))
y_euler[0] = 1

for i in range(1, len(t_euler)):
    y_euler[i] = y_euler[i-1] + h * (2 * y_euler[i-1])

# --- Resultados en consola ---
print("t\t Euler\t\t Exacto\t\t Error")
for i in range(len(t_euler)):
    exacto = np.exp(2 * t_euler[i])
    error = abs(y_euler[i] - exacto)
    print(f"{t_euler[i]:.1f}\t {y_euler[i]:.4f}\t\t {exacto:.4f}\t\t {error:.4f}")

# --- Gráfica ---
plt.plot(t_exacto, y_exacto, 'b-', label='Solución Exacta')
plt.plot(t_euler, y_euler, 'ro--', label='Método de Euler')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Separación de Variables vs Método de Euler')
plt.legend()
plt.grid(True)
plt.savefig('comparacion.png')
plt.show()
