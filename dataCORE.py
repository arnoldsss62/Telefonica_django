import pandas as pd
#Informacion_cmts=pd.read_excel('Listado de Nodos CMTS - Estacion.xlsx')
#Lista Locales de Energia
#local=Informacion_cmts['Nombre Local']
#Lista de CMTS
#CMTS=Informacion_cmts['Localidad']
#lISTA de CMTS 2
#cmts2=Informacion_cmts['CMTS']

df = pd.read_excel('Remedy.xlsx')
 
#Filtro Estado
df1=df[df['Estado REMEDY del dia']=='Programado']
df2=df[df['Estado REMEDY del dia']=='Programado para aprobación']
df3=df[df['Estado REMEDY del dia']=='Pendiente']
df4=df[df['Estado REMEDY del dia']=='Cerrado']

datafiltradariesgo =pd.concat([df1,df2,df3])

#Filtro TP que se encuentran en CMTS

dataCMTS=datafiltradariesgo[datafiltradariesgo['Nivel 3 (C. Prd)']=='OTS']
dataOLT=datafiltradariesgo[datafiltradariesgo['Nivel 3 (C. Prd)']=='CMTS']
#dataENERGIA=datafiltradariesgo[datafiltradariesgo['Nivel 1 (C. Prd)']=='ENERGIA']
datacorefija=pd.concat([dataCMTS, dataOLT]) #aumentar data energia

#Filtra trabajos con inicio y fin en un solo dia
datacorefija['diainicio'] = pd.DatetimeIndex(datacorefija['Fecha programada de inicio+']).day
datacorefija['diafinal'] = pd.DatetimeIndex(datacorefija['Fecha programada de finalización+']).day
diferencia=datacorefija['diainicio']-datacorefija['diafinal']

datacorefija['diferenciadia'] = pd.Series(diferencia)
datos=datacorefija[datacorefija['diferenciadia']==0]

#datos listos
del datos['diainicio']
del datos['diafinal']
del datos['diferenciadia']

#Filtrar registros que contengan locales principales de energia
datos_area=datos['Nivel 1 (C. Prd)']

datos_RESUMEN=datos['Resumen*'].str
datos_REMEDY=datos['ID del Cambio*+']
listaindices=list(datos_REMEDY.index.values)
datos_remitente=datos['Remitente*']
datos_grupoCoordinador=datos['Grupo coordinador*+']
datos_site=datos['Site']
datos_riesgo=datos['Nivel de riesgo*']
TiempoFechaFin=datos['Fecha programada de finalización+']
TiempoFechaInicio=datos['Fecha programada de inicio+']

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")

import django

django.setup()

import random
from  t_test.models import Cmts, Nodo, Troba, Usuario, InfoCore, TareaProgramada
import numpy as np
from django.conf import settings
from django.utils.timezone import make_aware

django.setup()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR= os.path.join(BASE_DIR,'Telefonica_django/media')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")
cd=len(datos)
def Populate(A):
#agregar cuando este data energia
#    for K in range(0,cd):
#
#       N=listaindices[K]
#        real_area=datos_area[N]
#        if real_area =='ENERGIA':
#            energia_local=datos_RESUMEN.str.lstrip('/')
    for K in range(0,A-1):
         #real_cmtsNombre=datos_Jefatura[N]
         #real_nodoNombre=datos_NODO[N]
         #real_trobaNombre=datos_TROBA[N]
         N=listaindices[K]
         real_area=datos_area[N]
         cmts=datos_RESUMEN.str.strip(': ')
         cmts1=cmts.str.lstrip('//')
         real_cmts=cmts1

         real_remitente=datos_remitente[N]
         real_remedy=datos_REMEDY[N]
         real_grupoCoordinador=datos_grupoCoordinador[N]
         real_site=datos_site[N]
         #real_riesgo=datos_riesgo[N]
         #usefin=TiempoFechaFin[N]
         #useinicio=TiempoFechaInicio[N]

         real_FechaInicio=TiempoFechaInicio[N]
         #real_horaInicio=useinicio.strftime("%H:%M:%S")
         #real_fechaFin=usefin.strftime("%H:%M:%S")
         real_horaInicio=TiempoFechaInicio[N]
         real_horaFin=TiempoFechaFin[N]

         cmts1=Cmts.objects.get_or_create(cmtsNombre=real_cmts)[0] 
         #Preguntar arnold como mapeara esta parte
         #nodo1=Nodo.objects.get_or_create(nodoNombre=real_nodoNombre,cmts =cmts1)[0]
         #troba1=Troba.objects.get_or_create(trobaNombre=real_trobaNombre,nodo=nodo1)[0]
         infoCore1=InfoCore.objects.get_or_create(remedy=real_remedy,remitente=real_remitente,grupoCoordinador=real_grupoCoordinador,site=real_site)[0]
         tareaProgramada=TareaProgramada.objects.get_or_create(fecha=real_FechaInicio ,horaInicio=real_horaInicio,horaFin=real_horaFin,infoCore=infoCore1,area=real_area)

if __name__ == '__main__':
    Populate(cd)

