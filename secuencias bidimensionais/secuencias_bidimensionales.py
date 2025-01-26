# Las secuencias bidimensionales (listas de listas) Son similares a una tabla o matriz. Aqui hay algunos ejemplos:

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz[0][1])

# Recorrido:
# Individual:

for fila in matriz:
    for valor in fila:
        print(valor, end="")
    print()

# Filas completas
for fila in matriz:
    print(fila)
    
# En funcion de la longitud

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()
    
# Otra forma de acceder a los elementos o crear matrices

nueva_matriz = [[x*2 for x in row]for row in matriz]
print(nueva_matriz)