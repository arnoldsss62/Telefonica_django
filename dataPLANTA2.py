import urllib.request
from os import remove
#modula de descraga de archivo de TP de Movistar1 diario
remove('ExcelMovistar1.xlsx')
aD='http://10.226.156.216:9571/noc/trabprog_noc.csv'
aG='ExcelMovistar1.csv'
descarga=urllib.request.urlopen(aD)
fichero=open(aG,'wb')
fichero.write(fG.read())
fichero.close()

#carga y definicion de campos de Movistar1
import pandas as pd
df=pd.read_csv("ExcelMovistar1.csv")
datos_Jefatura= df['Jefatura']
datos_NODO=df['NODO']
datos_TROBA=df['TROBA']
datos_ESTADO=df['ESTADO']
datos_CORTESN=df['CORTESN']
datos_TIPODETRABAJO=df['TIPODETRABAJO']
datos_REMEDY=df['REMEDY']
#Trabajos por horas, no se define dia de fin
datos_FINICIO=df['FINICIO']
datos_HINICIO=df['HINICIO']
datos_HTERMINO=df['HTERMINO']
listaindices=list(datos_REMEDY.index.values)

#conectar a la base de datos
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")

import django
django.setup()

from  t_test.models import Cmts, Nodo, Troba, InfoPlanta, TareaProgramada
import numpy as np
from django.conf import settings
from django.utils.timezone import make_aware

django.setup()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR= os.path.join(BASE_DIR,'Telefonica_django/media')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")
 
#carga de datos
def Populate(A):

    #indicar que es A
    for K in range(0,A):

         N=listaindices[K]
         real_cmtsNombre=datos_Jefatura[N]
         real_nodoNombre=datos_NODO[N]
         real_trobaNombre=datos_TROBA[N]
         real_estado=datos_ESTADO[N]
         real_corteS_N=datos_CORTESN[N]
         real_tipoTrabajo=datos_TIPODETRABAJO[N]
         real_remedy=datos_REMEDY[N]
         real_Fecha=datos_FINICIO[N]
         real_horaInicio=datos_HINICIO[N]
         real_horaFin=datos_HTERMINO[N]

         cmts1=Cmts.objects.get_or_create(cmtsNombre=real_cmtsNombre)[0]
         nodo1=Nodo.objects.get_or_create(nodoNombre=real_nodoNombre,cmts =cmts1)[0]
         troba1=Troba.objects.get_or_create(trobaNombre=real_trobaNombre,nodo=nodo1)[0]
         infoPlanta1=InfoPlanta.objects.get_or_create(remedy=real_remedy,estado=real_estado,corteS_N=real_corteS_N,tipoTrabajo=real_tipoTrabajo,troba=troba1)[0]
         tareaProgramada=TareaProgramada.objects.get_or_create(area='Planta',fecha=real_Fecha,horaFin=real_horaFin,horaInicio=real_horaInicio,infoPlanta=infoPlanta1)


if __name__ == '__main__':
    Populate(ctd)
