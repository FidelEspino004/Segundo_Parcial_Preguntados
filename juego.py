import pygame
import random
import json
from variables_funciones import *
from game_master import *
from preguntas import *

#-----------------------------------------MOSTAR MENU PRINCIPAL---------------------------------------
def mostrar_menu_principal():
    print(f"\n---- MENÚ PRINCIPAL ----")
    print(f"1. Jugar")
    print(f"2. Configurar Juego")
    print(f"3. TOP")
    print(f"4. Agregar Preguntas")
    print(f"5. Estadísticas de las Preguntas")
    print(f"6. Salir")
    print(' ')
    seleccion = input("Elige una opción: ")
    return seleccion
#-----------------------------------------MOSTAR MENU DE CONFIGURACION---------------------------------------
def mostrar_menu_configurar():
    print(f"\n---- CONFIGURAR JUEGO ----")
    print(f"1. Cantidad de Puntos por Respuesta Correcta")
    print(f"2. Cantidad de Vidas")
    print(f"3. Cantidad de Tiempo entre Preguntas")
    print(f"4. Volver al Menú Principal")
    print(' ')
    seleccion = input("Elige una opción: ")
    return seleccion
#------------------------------------------------EJECUTAR MENU-----------------------------------------------
def ejecutar():
    while True:
        seleccion = mostrar_menu_principal()
#-------------INICIAR JUEGO
        if seleccion == '1':
            print(f"\nIniciando el juego...")
            

#-------------CONFIGURAR JUEGO
        elif seleccion == '2':


            while True:
                seleccion_config = mostrar_menu_configurar()
                if seleccion_config == '1':
                    puntos = input("Introduce la cantidad de puntos por respuesta correcta: ")
                    print(f"Puntos por respuesta correcta configurados a: {puntos}")
                elif seleccion_config == '2':
                    vidas = input("Introduce la cantidad de vidas: ")
                    print(f"Vidas configuradas a: {vidas}")
                elif seleccion_config == '3':
                    tiempo = input("Introduce la cantidad de tiempo entre preguntas (en segundos): ")
                    print(f"Tiempo entre preguntas configurado a: {tiempo} segundos.")
                elif seleccion_config == '4':
                    break
                else:
                    print(' ')
                    print(f"Opción inválida. Por favor, elija una de las opciónes.")
#-------------MOSTRAR TOP                     
        elif seleccion == '3':
            print(f"\nMostrando el TOP de jugadores...")
#-------------AGREGAR PREGUNTAS
        elif seleccion == '4':
            print(f"\nAgregando preguntas...")
#------------ESTADISTICAS DE LAS PREGUNTAS
        elif seleccion == '5':
            print(f"\nMostrando estadísticas de las preguntas...")

        elif seleccion == '6':
            print(f"\nSaliendo del juego...")
            break
        else:
            print(' ')
            print(f"Opción inválida. Por favor, elija una de las opciónes.")

print(ejecutar())

pygame.init
"""
while Juego.corriendo():
    

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit
"""