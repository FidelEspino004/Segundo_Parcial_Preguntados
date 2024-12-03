import json
import pygame
import preguntas
import random
from preguntas import *
from variables_funciones import *

class Juego:

    def __init__(self, preguntas) :
        self.preguntas = []
        self.pregunta_actual = 0        
        self.jugador_nombre = ''
        self.jugador_puntuacion = 0
        self.corriendo = True
        self.preguntas_usadas = []

    def obtener_pregunta(self):
        preguntas_disponibles = [p for p in self.preguntas if p not in self.preguntas_usadas]

        if not preguntas_disponibles:
            return None

        pregunta = random.choice(preguntas_disponibles)

        self.preguntas_usadas.append(pregunta)

        return pregunta 

