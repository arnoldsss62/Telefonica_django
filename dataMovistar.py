#Script que carga la informacion de TP de Remedy 
import pandas as pd
Informacion_cmts=pd.read_excel('Listado de Nodos CMTS - Estacion.xlsx')
#Lista Locales de Energia
local=Informacion_cmts['Nombre Local']
#Lista de CMTS
CMTS=Informacion_cmts['Localidad']
#lISTA de CMTS 2
cmts2=Informacion_cmts['CMTS']

df = pd.read_excel('Remedy.xlsx')
 
#Filtro Estado
df1=df[df['Estado*']=='Programado']
df2=df[df['Estado*']=='Programado para aprobación']
df3=df[df['Estado*']=='Pendiente']
df4=df[df['Estado*']=='Cerrado']
datafiltradariesgo =pd.concat([df1,df2,df3])

#Filtro TP que se encuentran en CMTS
dataCMTS=datafiltradariesgo[datafiltradariesgo['Nivel 3 (C. Prd)']=='OTS']
dataOLT=datafiltradariesgo[datafiltradariesgo['Nivel 3 (C. Prd)']=='CMTS']
dataENERGIA=datafiltradariesgo[datafiltradariesgo['Nivel 1 (C. Prd)']=='ENERGIA']
datacorefija=pd.concat([dataCMTS, dataOLT, dataENERGIA]) #aumentar data energia

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
datos_RESUMEN=datos['Resumen*']
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
    for K in range(0,len(datos)):
        N=listaindices[K]
        real_area=datos_area[N]
        real_Resumen=datos_RESUMEN[N]
        real_remitente=datos_remitente[N]
        real_remedy=datos_REMEDY[N]
        real_grupoCoordinador=datos_grupoCoordinador[N]
        real_site=datos_site[N]
        real_FechaInicio=TiempoFechaInicio[N]
        real_horaInicio=TiempoFechaInicio[N]
        real_horaFin=TiempoFechaFin[N]
        if real_area =='ENERGIA':
            posicion=real_Resumen.find('/')
            energia_local=real_Resumen[0:posicion]
            #Busca el local de energia en los registros
            if energia_local in local:
                posicion_local=local.index('energia_local')
                cmts_1=CMTS[posicion_local]
                #Asociar mas cmts a los locales especificos
                if energia_local=='AREQUIPA CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='CHICLAYO CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='CHORRILLOS':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=''
                if energia_local=='CUSCO CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='HIGUERETA CT (CALLE 10)':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=CMTS[posicion_local+3]
                if energia_local=='LA MOLINA':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='LOS OLIVOS  CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='MAGDALENA CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='MIRAFLORES-GRIMALDO CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=''
                if energia_local=='MONTERRICO - U LIMA CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='EL RETABLO':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=CMTS[posicion_local+3]
                if energia_local=='RIMAC':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='SAN ISIDRO CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=''
                if energia_local=='SAN JOSE  CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=CMTS[posicion_local+3]
                if energia_local=='OPERADOR CLARO (SAN JUAN DE MIRAFLORES)':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=CMTS[posicion_local+3]
                if energia_local=='TRUJILLO CT /TRUJILLO_B':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=CMTS[posicion_local+2]
                    cmts_4=''
                if energia_local=='WASHINGTON II' or energia_local=='WASHINGTON I' or energia_local=='WASHINGTON III':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
                if energia_local=='ZARATE CT':
                    cmts_2=CMTS[posicion_local+1]
                    cmts_3=''
                    cmts_4=''
        
        else :
            posicion1=real_Resumen.find(':')
            posicion2=real_Resumen.find('/')
            cmts_1=real_Resumen[posicion1+1:posicion2]
            cmts_2=''
            cmts_3=''
            cmts_4=''

         cmts1=Cmts.objects.get_or_create(cmtsNombre=cmts_1)
         cmts2=Cmts2.objects.get_or_create(cmtsNombre2=cmts_2)
         cmts3=Cmts3.objects.get_or_create(cmtsNombre3=cmts_3)
         cmts4=Cmts4.objects.get_or_create(cmtsNombre4=cmts_4)
         #Preguntar arnold como mapeara esta parte
         #nodo1=Nodo.objects.get_or_create(nodoNombre=real_nodoNombre,cmts =cmts1)[0]
         #troba1=Troba.objects.get_or_create(trobaNombre=real_trobaNombre,nodo=nodo1)[0]
         infoCore1=InfoCore.objects.get_or_create(remedy=real_remedy,remitente=real_remitente,grupoCoordinador=real_grupoCoordinador,site=real_site)[0]
         tareaProgramada=TareaProgramada.objects.get_or_create(fecha=real_FechaInicio ,horaInicio=real_horaInicio,horaFin=real_horaFin,infoCore=infoCore1,area=real_area)

if __name__ == '__main__':
    Populate(cd)