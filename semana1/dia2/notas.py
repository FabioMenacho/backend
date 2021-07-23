# Ejercicio  para sacar promedio de notas

notas = []
totalNotas = int(input("Cuantas notas desea evaluar: "))
promedio = 0
for n in range(1,totalNotas+1):
    nota = int(input("nota " + str(n) + ": "))
    promedio += nota
    notas.append(nota)
promedio = promedio/totalNotas 
print(notas)
print("Máxima nota: " + str(max(notas)))
print("Mínima nota: " + str(min(notas)))
print("Promedio: " + str(promedio))