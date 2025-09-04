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

    # Verificamos si alguna nota es menor a 4
    df["notasBajo_4"] = df["notas"].apply(lambda lista:  any(nota < 4 for nota in lista))

    # Filtramos los estudiantes que tienen al menos una nota bajo 4
    estudiantesBajo_4 = df[df["notasBajo_4"] == True]

    # Contamos total de las filas
    totalFilas = len(df)

    # Contamos las notas bajo 4
    contNotasBajo_4 = df["notasBajo_4"].sum()

    # Calculamos el porcentaje
    porcentaje = (contNotasBajo_4 / totalFilas) * 100

    # Imprimimos los resultados
    print(estudiantesBajo_4[["nombre", "notas"]].to_string(index=False))
    print(f"Los estudiantes que tienen al menos una nota  bajo 4.0 son: {contNotasBajo_4} de {totalFilas}")
    print(f"Porcentaje: {round(porcentaje, 1)}%")
