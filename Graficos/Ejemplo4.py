import matplotlib.pyplot as plt
import numpy as np

# Datos
data = [3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 1, 2, 2]

# Crear el histograma
plt.hist(data, bins=5,color='black', edgecolor="gray")

# Agregar título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()