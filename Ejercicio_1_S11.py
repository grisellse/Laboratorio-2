import pandas as pd
import matplotlib.pyplot as plt

# https://www.kaggle.com/datasets/abdulszz/spotify-most-streamed-songs --- Se uso este DataSet


# Con esta line se carga el dataset
df = pd.read_csv("Spotify Most Streamed Songs.csv")

# Revisar solo las primeras filas del dataset
print(df.head())

# Contar el número de canciones por artista
artista_frecuencia = df['artist(s)_name'].value_counts().head(10)  # Mostramos solo los 10 artistas con mas streams en sus canciones

# Crear gráfico de barras
plt.figure(figsize=(10, 6))# Tamaño de la figura
artista_frecuencia.plot(kind='bar', color='lightblue')# le agrega el color al grafico
plt.title('Top 10 Canciones con mas streams por Artista')# le agrega el titulo al grafico
plt.xlabel('Artista')#le agrega el eje x al grafico
plt.ylabel('Cantidad de Canciones')# le agrega un label para al eje y
plt.show() # muestra el grafico


# ------------------Aqui va la grafica de lineas---------------------
# Obtener los 10 artistas más streamados y sus streams totales
artistas_top = df['artist(s)_name'].value_counts().head(10)
streams_por_artista = df.groupby('artist(s)_name')['streams'].sum().loc[artistas_top.index]

# Preparar los datos para el gráfico de líneas
x = range(1, len(streams_por_artista) + 1)  # Índices de los artistas
y = streams_por_artista.values  # Valores de streams

# Crear el gráfico de líneas
plt.plot(x, y, marker='o')  # Agregar marcador en cada punto
plt.title("Total de Streams de los 10 Artistas más Streamados")
plt.xlabel("Artistas")
plt.ylabel("Número de Streams")
plt.xticks(ticks=x, labels=streams_por_artista.index, rotation=45)  # Etiquetas de los artistas
plt.grid()  # Agregar una cuadrícula para mayor claridad
plt.show()

# ------------------Aqui va la grafica de pastel---------------------

frecuencia = df['artist(s)_name'].value_counts().head(10)  # Top 10 artistas
plt.figure(figsize=(8, 8))# ayuda a definir un tamanño para la grafica
plt.pie(frecuencia.values, labels=frecuencia.index, autopct="%1.1f%%", startangle=90)# ayuda a definir el tipo de grafica y el porcentaje que se muestra en la grafica
plt.title('Canciones de los 10 Artistas con más Streams')#ayuda a definir el titulo de la grafica
plt.show()#ayuda a mostrar la grafica
