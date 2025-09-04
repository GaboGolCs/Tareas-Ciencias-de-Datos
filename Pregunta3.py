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
    df = validadores.validarRango(df_estudiantesNotasFloat) 


except ValueError as dfVacio:
    print(dfVacio)


else:
    
    # Separamos todas las notas en una sola columna
    notas = df["notas"].explode()

    # Calculamos la(s) moda(s)
    moda = notas.mode().to_list()

    # Filtramos los estudiantes que tienen alguna de las notas moda
    df["tiene_moda"] = df["notas"].apply(lambda lista: any(nota in moda for nota in lista))
    estudiantes_moda = df[df["tiene_moda"]]

    # imprimimos resultados
    print(estudiantes_moda[["nombre", "notas"]].to_string(index=False))
    print("Las notas más frecuentes (moda) considerando todos los estudiantes son:", moda)
