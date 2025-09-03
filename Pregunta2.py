#Cuantos estudiantes aprobaron todas las asignaturas todas las notas >= 4.0
import pandas as pd
from statistics import mean
from datosEstudiantes import estudiantes
import validadores

def filtroNota(lista):
    return all(nota >= 4.0 for nota in lista)

try:
    #Validacion si se encuentra vacio
    vacio = validadores.estaVacio(estudiantes)
    if(vacio):
        raise ValueError("La lista se encuentra vacia")
    
    #Validacion de tipos float con transformacion
    df_estudiantesNotasFloat = validadores.validarFormatoListas(estudiantes)

    #Validacion de rangos de float entre 1 y 7
    dfEstudiantes = validadores.validarRango(df_estudiantesNotasFloat) 


except ValueError as dfVacio:
    print(dfVacio)


else:
    aprobadosBooleana = dfEstudiantes["notas"].apply(filtroNota)
    df_aprobados = dfEstudiantes[aprobadosBooleana]
    print(df_aprobados)
    print("Cantidad de estudiantes que aprobaron todo:", len(df_aprobados))
