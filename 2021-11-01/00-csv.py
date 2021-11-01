import csv

# Abrir archivo y lector
archivo = open('2021-11-01/00-datos.csv')
lector_csv = csv.reader(archivo, delimiter=',', quotechar='"')

# Leer encabezados
encabezados = next(lector_csv)
print('Encabezados: ' + str(encabezados))

# Leer filas
for fila in lector_csv:
    print('Nombre: {0}, Apellido: {1}, email: {2}'.format(fila[0], fila[1], fila[2]))

# Cerrar archivo
archivo.close()
