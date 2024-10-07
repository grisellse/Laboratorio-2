import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
df = pd.read_csv("Youtuber.csv")

# Revisar las primeras filas del dataset
print(df.head())

# Seleccionar los 10 YouTubers con más suscriptores
top_youtubers = df[['Channel Name', 'Subscribers']].sort_values(by='Subscribers', ascending=False).head(10)

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(top_youtubers['Channel Name'], top_youtubers['Subscribers'], color='skyblue')
plt.title('Top 10 YouTubers con más Suscriptores')
plt.xlabel('YouTuber')
plt.ylabel('Número de Suscriptores (millones)')
plt.xticks(rotation=45)
plt.show()
# Seleccionar los 10 YouTubers con más vistas totales
top_youtubers_vistas = df[['Channel Name', 'Average Views']].sort_values(by='Average Views', ascending=False).head(10)

# Preparar los datos para el gráfico de líneas
x = range(1, len(top_youtubers_vistas) + 1)
y = top_youtubers_vistas['Average Views']

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(x, y, marker='o', linestyle='-', color='green')
plt.title('Total de Vistas del Top 10 YouTubers')
plt.xlabel('YouTuber')
plt.ylabel('Total de Vistas (miles de millones)')
plt.xticks(ticks=x, labels=top_youtubers_vistas['Channel Name'], rotation=45)
plt.show()


# Seleccionar los 10 YouTubers con más suscriptores y sus categorías
top_youtubers_categoria = df[['Channel Name', 'Category']].value_counts().head(10)

# Crear gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(top_youtubers_categoria.values, labels=top_youtubers_categoria.index, autopct='%1.1f%%', startangle=90)
plt.title('Proporción de Categorías en el Top 10 YouTubers')
plt.show()
