# -*- coding: utf-8 -*
"""
Spyder Editor

This is a temporary script file.
"""
#Función que saca el promedio de entre cinco notas, eliminando la menor de ellas
def nota_quices(codigo: str, nota1: int, nota2: int, nota3: int, nota4: int, nota5: int) -> str:
    promedio = round((((nota1 + nota2 + nota3 + nota4 + nota5) - min(nota1,nota2,nota3,nota4,nota5)) / 20) / 4, 2)
    return("El promedio ajustado del estudiante {} es: {}".format(codigo, promedio))

print(nota_quices("MA00201520", 40,50,39,76,96))