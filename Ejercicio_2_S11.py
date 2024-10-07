import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("disney_movies.csv")

# Revisar solo las primeras filas del dataset
print(df.head())

# Seleccionar solo las primeras 10 películas
df_top10 = df.head(10)

# 1. Gráfico de Barras: Total de ganancias ajustadas por inflación de las películas
ganancias = df_top10['inflation_adjusted_gross']  # Ganancias ajustadas por inflación
plt.figure(figsize=(12, 6))  # Tamaño de la figura
plt.bar(df_top10['movie_title'], ganancias, color='lightblue')  # Crear gráfico de barras
plt.title('Ganancias Ajustadas por Inflación de las Primeras 10 Películas de Disney')  # Título del gráfico
plt.xlabel('Película')  # Etiqueta para el eje X
plt.ylabel('Ganancias Ajustadas (USD)')  # Etiqueta para el eje Y
plt.xticks(rotation=45)  # Rotar etiquetas del eje X
plt.show()  # Muestra el gráfico


# 2. Gráfico de Líneas: Total de ganancias de las películas
x = range(1, len(ganancias) + 1)  # Eje X (número de películas)
y = ganancias.values  # Ganancias ajustadas

plt.figure(figsize=(12, 6))  # Tamaño de la figura
plt.plot(x, y, marker='o', color='purple')  # Gráfico de líneas
plt.title('Ganancias Totales de las Primeras 10 Películas de Disney')  # Título del gráfico
plt.xlabel('Película')  # Etiqueta para el eje X
plt.ylabel('Ganancias Totales (USD)')  # Etiqueta para el eje Y
plt.xticks(ticks=x, labels=df_top10['movie_title'], rotation=45)  # Etiquetas de las películas
plt.grid()  # Agregar cuadrícula
plt.show()  # Muestra el gráfico


# 3. Gráfico Circular: Proporción de géneros de las películas
generos = df_top10['genre'].value_counts()  # Contar géneros de película
plt.figure(figsize=(8, 8))  # Tamaño de la figura
plt.pie(generos.values, labels=generos.index, autopct="%1.1f%%", startangle=90)  # Gráfico de pastel
plt.title('Proporción de Géneros de las Primeras 10 Películas de Disney')  # Título del gráfico
plt.show()  # Muestra la gráfica
