import json
import pygame
import random
from variables_funciones import *


class preguntas_clase:
    def __init__(self, pregunta):
        self.pregunta = pregunta['pregunta']
        self.dificultad = pregunta['dificultad']
        self.respuestas = pregunta['respuestas']
        self.correcta = pregunta['respuesta_correcta']

    def validacion_pregunta(self, respuesta_elejida):
        if respuesta_elejida == self.correcta:
            return True
        else:
            return False
    

preguntas = [
    {
        'pregunta': '¿Cuál es la capital de Francia?',
        'dificultad':'facil',
        'respuestas': [
            'A. Madrid',
            'B. París',
            'C. Londres',
            'D. Roma'        ],
        'respuesta_correcta': 'B'
    },
    {
        'pregunta': '¿Quién escribió "Don Quijote de la Mancha"?',
        'dificultad':'media',
        'respuestas': [
            'A. Garcilaso de la Vega',
            'B. Miguel de Cervantes',
            'C. Lope de Vega',
            'D. Felipe González'
        ],
        'respuesta_correcta': 'B'
    },
    {
        'pregunta': '¿En qué año comenzó la Segunda Guerra Mundial?',
        'dificultad':'media',
        'respuestas': [
            'A. 1914',
            'B. 1939',
            'C. 1945',
            'D. 1923'
        ],
        'respuesta_correcta': "B"
    },
    {
        'pregunta': '¿Cuál es el metal más pesado?',
        'dificultad':'facil',
        'respuestas': [
            'A. Oro',
            'B. Plomo',
            'C. Mercurio',
            'D. Osmio'
        ],
        'respuesta_correcta': 'D'
    },
    {
        'pregunta': '¿Cuántos planetas hay en el sistema solar?',
        'dificultad':'media',
        'respuestas': [
            'A. 7',
            'B. 8',
            'C. 9',
            'D. 10'
        ],
        'respuesta_correcta': 'B'
    },
    {
        'pregunta': '¿Cuál es el símbolo químico del oxígeno?',
        'dificultad':'facil',
        'respuestas': [
            'A. O',
            'B. O2',
            'C. Ox',
            'D. Oxy'
        ],
        'respuesta_correcta': 'A'
    },
    {
        'pregunta': '¿Qué escritor creó a Sherlock Holmes?',
        'dificultad':'media',
        'respuestas': [
            'A. J.R.R. Tolkien',
            'B Agatha Christie',
            'C. Arthur Conan Doyle',
            'D. Edgar Allan Poe'
        ],
       'respuesta_correcta': 'C'
    },
    {
        'pregunta': '¿Cuál es la lengua oficial de Brasil?',
        'dificultad':'facil',
        'respuestas': [
            'A. Español',
            'B. Portugués',
            'C. Francés',
            'D. Inglés'
        ],
        'respuesta_correcta': 'B'
    },
    {
        'pregunta': '¿Qué instrumento musical tiene 88 teclas?',
        'dificultad':'facil',
        'respuestas': [
            'A. Guitarra',
            'B. Piano',
            'C. Violín',
            'D. Flauta'
        ],
        'respuesta_correcta': 'B'
    },
    {
        'pregunta': '¿Quién pintó la Mona Lisa?',
        'dificultad':'facil',
        'respuestas': [
            'A. Leonardo da Vinci',
            'B. Vincent van Gogh',
            'C. Pablo Picasso',
            'D. Claude Monet'
        ],
        'respuesta_correcta': 'A'
    }
]

with open('preguntas.json', 'w') as archivo:
    json.dump(preguntas, archivo)