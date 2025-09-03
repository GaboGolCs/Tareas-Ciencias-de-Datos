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
    df_estudiantesLimpios = validadores.validarRango(df_estudiantesNotasFloat) 


except ValueError as dfVacio:
    print(dfVacio)

else:
    df_estudiantesLimpios["promedios"] = df_estudiantesLimpios["notas"].apply(mean)
    df_estudiantesLimpios["promedios"] = df_estudiantesLimpios["promedios"].round(1)

    print("Promedio de notas de los estudiantes:\n",df_estudiantesLimpios)

    promedioMasAlto = df_estudiantesLimpios["promedios"].max()
    promedioMasBajo = df_estudiantesLimpios["promedios"].min()

    promedioMasAlto = round(promedioMasAlto,1)
    promedioMasBajo = round(promedioMasBajo,1)

    print("El promedio mas alto es: ", promedioMasAlto)
    print("El promedio mas bajo es: ", promedioMasBajo)
