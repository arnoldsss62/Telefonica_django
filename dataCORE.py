import pandas as pd

df = pd.read_excel('Remedy.xlsx')

#Filtro Estado
df1=df[df['Estado*']=='Programado']
df2=df[df['Estado*']=='Programado para aprobación']
df3=df[df['Estado*']=='Pendiente']
df4=df[df['Estado*']=='False']
df5=pd.concat([df1,df2,df3,df4])

#Filtro Riesgo
df6 = df5[df5['Nivel de riesgo*'] == 'Nivel de riesgo 4']
df7 = df5[df5['Nivel de riesgo*'] == 'Nivel de riesgo 5']
df8 = df5[df5['Nivel de riesgo*'] == 'Nivel de riesgo 3']
datafiltradariesgo = pd.concat([df6, df7, df8])

#Filtro Core
dataipfija=datafiltradariesgo[datafiltradariesgo['Nivel 1 (C. Prd)']=='CORE IP FIJA']
datavozfija=datafiltradariesgo[datafiltradariesgo['Nivel 1 (C. Prd)']=='CORE VOZ FIJA']
datafiltrada1=pd.concat([dataipfija, datavozfija])

#Filtra trabajos con inicio y fin en un solo dia
datafiltrada1['diainicio'] = pd.DatetimeIndex(datafiltrada1['Fecha programada de inicio+']).day
datafiltrada1['diafinal'] = pd.DatetimeIndex(datafiltrada1['Fecha programada de finalización+']).day
diferencia=datafiltrada1['diainicio']-datafiltrada1['diafinal']

datafiltrada1['diferenciadia'] = pd.Series(diferencia)
datos=datafiltrada1[datafiltrada1['diferenciadia']==0]


#datos listos
del datos['diainicio']
del datos['diafinal']
del datos['diferenciadia']

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

def Populate(A):
    for K in range(0,A-1):
         #real_cmtsNombre=datos_Jefatura[N]
         #real_nodoNombre=datos_NODO[N]
         #real_trobaNombre=datos_TROBA[N]
         N=listaindices[K]

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

         #cmts1=Cmts.objects.get_or_create(cmtsNombre="Null")[0]
         #nodo1=Nodo.objects.get_or_create(nodoNombre=real_nodoNombre,cmts =cmts1)[0]
         #troba1=Troba.objects.get_or_create(trobaNombre=real_trobaNombre,nodo=nodo1)[0]

         infoCore1=InfoCore.objects.get_or_create(riesgo=4,remedy=real_remedy,remitente=real_remitente,grupoCoordinador=real_grupoCoordinador,site=real_site)[0]

         tareaProgramada=TareaProgramada.objects.get_or_create(fecha=real_FechaInicio ,horaInicio=real_horaInicio,horaFin=real_horaFin,infoCore=infoCore1,area="Core")

if __name__ == '__main__':

    print('Populando la DB')
    cd=len(datos)-1
    Populate(cd)
