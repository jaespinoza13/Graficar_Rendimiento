import matplotlib.pyplot as plt

# Datos de ejemplo
niveles_k = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
datafly_tiempos = [0.5, 0.6, 0.55, 0.58, 0.59, 0.6, 0.62, 0.65, 0.67, 0.7]
mondrian_tiempos = [0.4, 0.5, 0.45, 0.48, 0.49, 0.52, 0.54, 0.57, 0.6, 0.63]
incognito_tiempos = [0.4, 0.5, 0.45, 0.48, 0.49, 0.52, 0.54, 0.57, 0.6, 0.63]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Graficar tiempo de ejecución
ax.set_xlabel('Nivel de k')
ax.set_ylabel('Tiempo de Ejecución (s)', color='tab:blue')
ax.plot(niveles_k, datafly_tiempos, label='Datafly - Tiempo', color='tab:blue')
ax.plot(niveles_k, mondrian_tiempos, label='Mondrian - Tiempo', color='tab:orange', linestyle='dashed')
ax.plot(niveles_k, incognito_tiempos, label='Incognito - Tiempo', color='tab:green', linestyle='dotted')
ax.tick_params(axis='y', labelcolor='tab:blue')

# Agregar leyendas
fig.tight_layout()  # Para que no se solapen las etiquetas
fig.legend(loc='upper left', bbox_to_anchor=(0.1,0.9))

plt.title('Comparación de Tiempo de Ejecución de Anonimización')
plt.show()
