import numpy as np
import matplotlib.pyplot as plt

# Crear valores para la curva
t = np.linspace(0, 2 * np.pi, 1000)

# Ecuaciones paramétricas del corazón
x = 16 * np.sin(t)**3
y = (
    13 * np.cos(t)
    - 5 * np.cos(2 * t)
    - 2 * np.cos(3 * t)
    - np.cos(4 * t)
)

# Crear la gráfica
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red', linewidth=3)

# Rellenar el corazón
plt.fill(x, y, color='pink', alpha=0.8)

# Ajustes visuales
plt.title("Te extraño Sofi")
plt.axis('equal')   # Mantener proporciones
plt.axis('off')     # Ocultar ejes

# Mostrar
plt.show()