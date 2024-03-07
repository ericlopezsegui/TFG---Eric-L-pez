import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect('database.db')

# Crear un objeto cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar una consulta
cursor.execute('SELECT * FROM Arbit')

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()
