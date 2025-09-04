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
    df = pd.DataFrame(estudiantes)

    # Calculamos el promedio de cada estudiante
    df["promedio"] = df["notas"].apply(lambda lista: sum(lista) / len(lista))

    # Calculamos el promedio general del curso
    promedio_general = df["promedio"].mean()

    # Imprimimos los resultados
    print(df[["nombre", "notas", "promedio"]].round(1).to_string(index=False),"\n")
    print("Promedio general del curso es:", round(promedio_general, 1))
