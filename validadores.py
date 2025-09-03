import pandas as pd
def estaVacio(estudiantes):
    df_estudiantes = pd.DataFrame(estudiantes)
    if(df_estudiantes.empty):
        return True
    else:
        False

def validarFormatoListas(estudiantes):
    df_estudiantes = pd.DataFrame(estudiantes)
    mascara = df_estudiantes["notas"].apply(mascaraSoloFloat)
    df_filtrado = df_estudiantes[mascara]
    return df_filtrado

def mascaraSoloFloat(notas):
     return all(isinstance(nota, float) for nota in notas)


def validarRango(estudiantes):
    df_estudiantes = pd.DataFrame(estudiantes)
    mascara = df_estudiantes["notas"].apply(mascaraNotas)
    return df_estudiantes[mascara]


def mascaraNotas(notas):
        return all(isinstance(nota, float) and 1.0 <= nota <= 7.0 for nota in notas)

def limpiarListas(estudiantes):
    df_estudiantes = pd.DataFrame(estudiantes)
    def solo_numeros(lista):
        return [float(nota) for nota in lista if isinstance(nota, (int, float)) or (isinstance(nota, str) and nota.replace('.', '', 1).isdigit())]
    df_estudiantes["notas"] = df_estudiantes["notas"].apply(solo_numeros)
    return df_estudiantes