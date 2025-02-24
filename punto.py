"""
dado el archivo texto files/salesjan200p.csv procese el archivo para obtener
las compras realizadas en un pais dado 
"""

def obtener_compras_por_pais(pais):
    conteo = 0
    with open("C:\Users\Estudiante\Downloads\SalesJan2009.csv", 'r', encoding='utf-8') as file:
        headers = file.readline().strip().split(',')
        for linea in file:
            row = linea.strip().split(',')
            if len(row) > 7 and row[7] == pais:
                conteo += 1
    return conteo

pais = input('Ingrese el país a filtrar: ')
conteo_transacciones = obtener_compras_por_pais(pais)
print(f'El total de transacciones en {pais} es: {conteo_transacciones}')
