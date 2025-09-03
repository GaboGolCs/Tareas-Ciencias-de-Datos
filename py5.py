#Entrega un listado ordenado de mayor a menor con el promedio de los estudiantes
import pandas as pd
from statistics import mean
from datosEstudiantes import estudiantes
import validadores

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
    dfEstudiantes["promedios"] = dfEstudiantes["notas"].apply(mean)
    df_estudiantesOrdenados = dfEstudiantes.sort_values(by="promedios", ascending=False)
    df_estudiantesOrdenados["promedios"] = dfEstudiantes["promedios"].round(1)
    print("Estudiantes ordenados de mayor a menor por promedio:\n",df_estudiantesOrdenados)

   