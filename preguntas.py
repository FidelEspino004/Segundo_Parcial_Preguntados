from variables_funciones import *
import json

class preguntas:
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
        "pregunta": "¿Cuál es la capital de Francia?",
        'dificultad':'facil',
        "respuestas": [
            "Madrid",
            "París",
            "Londres",
            "Roma"
        ],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?",
        'dificultad':'media',
        "respuestas": [
            "Garcilaso de la Vega",
            "Miguel de Cervantes",
            "Lope de Vega",
            "Felipe González"
        ],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        'dificultad':'media',
        "respuestas": [
            "1914",
            "1939",
            "1945",
            "1923"
        ],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el metal más pesado?",
        'dificultad':'facil',
        "respuestas": [
            "Oro",
            "Plomo",
            "Mercurio",
            "Osmio"
        ],
        "respuesta_correcta": "D"
    },
    {
        "pregunta": "¿Cuántos planetas hay en el sistema solar?",
        'dificultad':'media',
        "respuestas": [
            "7",
            "8",
            "9",
            "10"
        ],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Cuál es el símbolo químico del oxígeno?",
        'dificultad':'facil',
        "respuestas": [
            "O",
            "O2",
            "Ox",
            "Oxy"
        ],
        "respuesta_correcta": "A"
    },
    {
        "pregunta": "¿Qué escritor creó a Sherlock Holmes?",
        'dificultad':'media',
        "respuestas": [
            "J.R.R. Tolkien",
            "Agatha Christie",
            "Arthur Conan Doyle",
            "Edgar Allan Poe"
        ],
        "respuesta_correcta": "C"
    },
    {
        "pregunta": "¿Cuál es la lengua oficial de Brasil?",
        'dificultad':'facil',
        "respuestas": [
            "Español",
            "Portugués",
            "Francés",
            "Inglés"
        ],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Qué instrumento musical tiene 88 teclas?",
        'dificultad':'facil',
        "respuestas": [
            "Guitarra",
            "Piano",
            "Violín",
            "Flauta"
        ],
        "respuesta_correcta": "B"
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        'dificultad':'facil',
        "respuestas": [
            "Leonardo da Vinci",
            "Vincent van Gogh",
            "Pablo Picasso",
            "Claude Monet"
        ],
        "respuesta_correcta": "A"
    }
]

with open('preguntas.json', 'w') as archivo:
    json.dump(preguntas, archivo)