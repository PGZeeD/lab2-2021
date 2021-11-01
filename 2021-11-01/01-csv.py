import csv

# Abrir archivo y escritor
archivo = open('2021-11-01/01-datos.csv', 'w', newline='')
escritor_csv = csv.writer(archivo, delimiter=',', quotechar='"')

# Escribir los datos
escritor_csv.writerow(['jose', 'sanchez', 'js@correo.com'])
escritor_csv.writerow(['pepe', 'perez', 'pp@correo.com'])
escritor_csv.writerow(['matias', 'de, la puente', 'mp@correo.com'])

# Cerrar archivo
archivo.close()

