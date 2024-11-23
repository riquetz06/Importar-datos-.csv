# Define la ruta del archivo CSV
file_path = 'ruta/al/archivo.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(file_path)
# Mostrar las primeras filas del DataFrame
print(df.head())

# Leer el archivo CSV en la misma carpeta de ejecición del script
file_path = 'datos.csv'
df = pd.read_csv(file_path)
# Mostrar las primeras filas del DataFrame
print(df.head())
