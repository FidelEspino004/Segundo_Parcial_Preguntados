import json


def traer_preguntas():
    print('a')
    #json.load
    #json -> diccionario return lista de diccionario
    #manejo de archivo 

def guardar_preguntas(pregunta):
    print('B')
    #manejo de archivo
    #json.dump = guardar preguntas

preguntas = [
    {
        "pregunta":"inserte pregunta 1",
        "respuesta_a":"inserte respuesta a",
        "respuesta_b":"inserte respuesta b",
        "respuesta_c":"inserte respuesta c",
        "respuesta_d":"inserte respuesta d"
    },
    {
        "pregunta":"inserte pregunta 2",
        "respuesta_a":"inserte respuesta a",
        "respuesta_b":"inserte respuesta b",
        "respuesta_c":"inserte respuesta c",
        "respuesta_d":"inserte respuesta d"
    },
    {
        "pregunta":"inserte pregunta 3",
        "respuesta_a":"inserte respuesta a",
        "respuesta_b":"inserte respuesta b",
        "respuesta_c":"inserte respuesta c",
        "respuesta_d":"inserte respuesta d"
    },
    {
        "pregunta":"inserte pregunta 4",
        "respuesta_a":"inserte respuesta a",
        "respuesta_b":"inserte respuesta b",
        "respuesta_c":"inserte respuesta c",
        "respuesta_d":"inserte respuesta d"
    },
    {
        "pregunta":"inserte pregunta 5",
        "respuesta_a":"inserte respuesta a",
        "respuesta_b":"inserte respuesta b",
        "respuesta_c":"inserte respuesta c",
        "respuesta_d":"inserte respuesta d"
    },
]

def recorrer_pregunta(preguntas:list, pregunta_actual:int):
    for pregunta in preguntas:
        if pregunta_actual == preguntas.index(pregunta):
            print(logica_pregunta)
    
