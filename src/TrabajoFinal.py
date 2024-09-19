# @markdown ## **Ejecutar esta celda (►)**
# @markdown
# @markdown Doble clic en mí y podrás ver mi código.
# =====================================================================================================================
# REGION: Congiguración de la consola
# =====================================================================================================================
from rich.console import Console
from rich.theme import Theme
from rich.progress import Progress
TemaAnalisisDatos = Theme({
    "info": "bold navy_blue on grey82",
    "url": "underline blue",
    "warning": "dark_orange",
    "danger": "bold red",
    "normalb": "bold black",
    "normal": "black"
}, inherit=False)
console = Console(theme=TemaAnalisisDatos)
# =====================================================================================================================
# REGION: Librerías
# =====================================================================================================================
with console.status("Cargando Librerías", spinner="clock"):
    import os
    import random as rnd
    import pandas as pd
    import time
    import logging
    import tqdm
    import rich
    import numpy as np
    import matplotlib.pyplot as plt
    import statistics as st
    import math as mt
    # from google.colab import drive
    import sys
    import datetime
    import time
    from tqdm import tqdm
    #import ace_tools as tools
    from collections import Counter
    inicio = time.time()
    import warnings
    # Ignorar todos los warnings
    warnings.filterwarnings("ignore")
# =====================================================================================================================
# REGION: Librerías
# =====================================================================================================================
console.print("Librerías cargadas satisfactoriamente", style="info")
# @markdown ## **Ejecutar esta celda (►)**
# @markdown
# @markdown Doble clic en mí y podrás ver mi código.
# =====================================================================================================================
# REGION: Funciones Útiles para Taller Proyecto Integrador
# NOTA: Las funciones fueron comentadas con GitHub Copilot
# =====================================================================================================================
def GenerarNombre(Nombres: list, Apellidos: list) -> str:
    """
    Genera un nombre completo seleccionando aleatoriamente un nombre y un apellido de las listas proporcionadas.

    Args:
        Nombres (list): Lista de nombres posibles.
        Apellidos (list): Lista de apellidos posibles.

    Returns:
        str: Un nombre completo en el formato 'Nombre Apellido'.
    """
    Nombre = rnd.choice(Nombres)
    Apellido = rnd.choice(Apellidos)
    return f'{Nombre} {Apellido}'

def GenerarEdad() -> int:
    """
    Genera una edad aleatoria basada en probabilidades predefinidas.

    Returns:
        int: Una edad aleatoria en uno de los siguientes rangos:
             - 16 a 25 años (50% de probabilidad)
             - 26 a 33 años (25% de probabilidad)
             - 34 a 40 años (15% de probabilidad)
             - 41 a 105 años (10% de probabilidad)
    """
    r = rnd.random()
    if r < 0.5:
        return rnd.randint(16, 25)
    elif r < 0.75:
        return rnd.randint(26, 33)
    elif r < 0.9:
        return rnd.randint(34, 40)
    else:
        return rnd.randint(41, 105)

def GenerarHoraAtencion_Lista() -> list:
    """
    Genera una lista de posibles horas de atención en intervalos de 20 minutos.

    Returns:
        list: Una lista de listas, donde cada sublista contiene una hora y un minuto en el formato [hora, minuto].
              Las horas van de 7 a 18 (inclusive) y los minutos pueden ser 0, 20 o 40.
    """
    horas = [x for x in range(7,19)]
    minutos = [0,20,40]
    citas_list = []
    for hora in horas:
        for minuto in minutos:
            citas_list.append([hora,minuto])
    return citas_list

def GenerarHoraAtencion_str() -> list:
    """
    Genera una lista de posibles horas de atención en formato de cadena.

    Returns:
        list: Una lista de cadenas, donde cada cadena representa una hora de atención en el formato "HH:MM".
              Las horas van de 7 a 18 (inclusive) y los minutos pueden ser 0, 20 o 40.
    """
    horas = [x for x in range(7,19)]
    minutos = [0,20,40]
    citas_list = []
    citas_str = []
    for hora in horas:
        for minuto in minutos:
            citas_list.append([hora,minuto])
    for hora, minuto in citas_list:
        citas_str.append(datetime.time(hora, minuto).strftime("%H:%M"))
    return citas_str

def SiguienteSemana():
    """
    Calcula las fechas de la próxima semana (de lunes a domingo) a partir de la fecha actual.

    Returns:
        list: Una lista de cadenas, donde cada cadena representa una fecha de la próxima semana en el formato "YYYY-MM-DD".
    """
    hoy = datetime.date.today()
    dia_semana = hoy.weekday()
    diferencia = (0 - dia_semana) % 7
    # Sumamos la diferencia a la fecha actual
    semana = []
    semana.append(str(hoy + datetime.timedelta(days=diferencia)))
    for i in range(1,7):
        semana.append(str(hoy + datetime.timedelta(days=diferencia+i)))
    return semana
  
  # =====================================================================================================================
# REGION: Log
# =====================================================================================================================
console.print(f'{"Inicio del proceso"}', style="info")
console.print(f'\t{"Log"}', style="danger")
inicio = time.time() #Inicio contador de ejecucion
hoy = datetime.date.today().strftime('%Y%m%d') #Captura de fecha de ejecucion
nombre_archivo_log = f"log_{hoy}.log" # Inicializacion del log
#Configuracion de almacenamiento y niveles del log
logging.basicConfig(filename=nombre_archivo_log, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#Primer registro del log
logging.info(f"Iniciando el proceso del log __{hoy}__ ")
# =====================================================================================================================
# REGION: Ubicacion y registro de archivos
# =====================================================================================================================
#Creamos el directorio (carpeta) en donde se crearan los archivos
console.print(f'\t{"Ubicacion y registro de archivos"}', style="danger")
DirectorioActual = os.getcwd() #Directorio actual de trabajo
textemp = f'El directorio actual de trabajo es: \n\t--> {DirectorioActual}, \nEsta carpeta contendrá los archivos del trabajo final'
logging.info(textemp) #Registro del directorio actual
#Creamos una carpeta donde almacenamos los resultados
CarpetaNueva = "CarpetaArchivosTrabajoFinal"
os.makedirs(CarpetaNueva, exist_ok=True) #Creamos la carpeta si no existe
logging.info("Se crea el directorio {}".format(CarpetaNueva)) #Registro de la creacion de la carpeta
# Nombre de la carpeta donde se crearán los archivos
carpeta = os.path.join(DirectorioActual, "CarpetaArchivosTrabajoFinal") #Ruta de la carpeta
logging.info("La ruta de trabajo será {}".format(carpeta)) #Registro de la ruta de trabajo
#Usamos los datos de GitHub con nombres y apellidos para leerlos.
RutaNombres = r'https://raw.githubusercontent.com/juliancastillo-udea/AlDiSi/main/Data/NombresArgentina.csv'
RutaApellidos = r'https://raw.githubusercontent.com/juliancastillo-udea/AlDiSi/main/Data/ApellidosArgentina.csv'
# =====================================================================================================================
# REGION: Creando datos genericos
# =====================================================================================================================
console.print(f'\t{"Creando datos genericos"}', style="danger")
logging.info("Cargando CSV con nombres")
dfNombres = pd.read_csv(RutaNombres, encoding='ISO-8859-1')
Nombres = dfNombres['name'].tolist()
logging.info("Reemplazando nombres y detalles del documento")
for i in tqdm(range(len(Nombres)), '\tProcesando nombres'):
    if ' ' in Nombres[i]:
        Nombres[i]=Nombres[i].replace(' ', '_')
logging.info("Cargando CSV con apellidos")
dfApellidos = pd.read_csv(RutaApellidos, encoding='ISO-8859-1')
Apellidos = dfApellidos['lastname'].tolist()
logging.info("Reemplazando apellidos y detalles del documento")
for i in tqdm(range(len(Apellidos)), '\tProcesando apellidos'):
    if ' ' in Apellidos[i]:
        Apellidos[i]=Apellidos[i].replace(' ', '_')
logging.info("Finalizado proceso de gestion de nombres y apellidos")
# endregion Gestion de archivos y ubicaciones
logging.info("Creando secuencia de citas")
horarioatencion = GenerarHoraAtencion_str()
semana = SiguienteSemana()
citas = []
for dia in semana:
    for cita in horarioatencion:
        citas.append(dia+'|'+cita)
# =====================================================================================================================
# REGION: Creacion del dataframe
# =====================================================================================================================
console.print(f'\t{"Creacion del dataframe"}', style="danger")
logging.info("Creando DataFrame con datos de citas y personas")
df = pd.DataFrame(columns=['Nombre', 'Edad', 'Fecha', 'CitaAtencion'])
for cita in citas:
    nombre = GenerarNombre(Nombres, Apellidos).upper()
    edad = GenerarEdad()
    fecha = datetime.date.today().strftime('%Y-%m-%d')
    atencion = cita
    vector = [nombre, edad, fecha, atencion]
    df.loc[len(df)] = vector
logging.info("finalizado proceso de creacion de dataframe")
fin = time.time()
delta = fin-inicio
console.print(f'\t{"Fin dataframe"}', style="danger")
minutos, segundos = divmod(delta, 60)

console.print(f'\tTiempo de ejecucion: {int(minutos)} minutos y {segundos:.2f} segundos', style="url")
logging.info("Exportar DataFrame a Excel y CSV")
df.to_excel(os.path.join(carpeta,'Citas.xlsx'))
df.to_csv(os.path.join(carpeta,'Citas.csv'))
logging.info("Finalizado")
console.print(f'{"Fin del proceso"}', style="info")
# =====================================================================================================================
# REGION: Fin
# ==============================================================================================
