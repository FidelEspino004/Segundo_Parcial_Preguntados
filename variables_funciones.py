from preguntas import *
import json

#CONTADORES---------
vidas = 3
tiempo = 30
#ACUMULADORES-------
puntuacion = 0

#------------------
bandera = 'si'
puntos_obtenidos = 0

def agregar_preguntas():
    while bandera == 'si':
        with open('preguntas.json', 'r') as archivo:
            preguntas = json.load(archivo)

        nueva_pregunta = {
            "pregunta": input("Ingresa la pregunta: "),
            "dificultad": input("Ingresa la dificultad (facil, media, dificil): "),
            "respuestas": {
                "A": input("Opción A: "),
                "B": input("Opción B: "),
                "C": input("Opción C: "),
                "D": input("Opción D: ")
            },
            "respuesta_correcta": input("Ingresa la opción correcta (A, B, C, D): ").upper()
        }

        preguntas.append(nueva_pregunta)

        with open('preguntas.json', 'w') as archivo:
            json.dump(preguntas, archivo)

        print("¡Pregunta agregada con éxito!")
        print(" ")
        bandera = input('¿Quiere agregar otra pregunta? (si o no): ')

        if bandera != 'si' and bandera != 'no' and bandera != 'Si' and bandera != 'No':
            bandera = input('Elija una de las opciones dadas (si o no): ')
        elif bandera == 'no' or bandera == 'No':
            print(" ")
            print('¡Listo!')
            print('Gracias por agregar una pregunta')


