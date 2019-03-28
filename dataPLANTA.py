import pandas as pd
from configparser import ConfigParser
from datetime import datetime
import os
from  t_test.models import Cmts, Nodo, Troba, Usuario, InfoPlanta, TareaProgramada
from random import randrange,choice
import numpy as np
from django.conf import settings
from django.utils.timezone import make_aware
import django


def Populate(A):
    django.setup()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_DIR= os.path.join(BASE_DIR,'Telefonica_django/media')

    df=pd.read_excel(MEDIA_DIR+"ExcelMovistar1.xlsx")

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


    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")

    #indicar que es A
    for N in range(0,A):

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
         tareaProgramada=TareaProgramada.objects.get_or_create(area="Planta",fecha=real_Fecha,horaFin=real_horaFin,horaInicio=real_horaInicio,infoPlanta=infoPlanta1)


if __name__ == '__main__':


    print('Populando la DB')
    print(len(df))
    ctd=len(df)
    Populate(ctd)
