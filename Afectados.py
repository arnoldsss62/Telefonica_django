import pandas as pd

df=pd.read_excel("Afectados1.xlsx")
datos=df

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")
import django

django.setup()

import random
from  t_test.models import Cmts, Nodo, Troba, Usuario, Afectados
import numpy as np
from django.conf import settings
from django.utils.timezone import make_aware

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR= os.path.join(BASE_DIR,'Telefonica_django/media')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")
def Populate(A):

    Fecha= datos['Fecha']
    Hora=datos['Hora']
    DURACION=datos['DURACION']
    CODIGO_CLIENTE=datos['CODIGO_CLIENTE']
    NOMBRE_CLIENTE=datos['CNT_NOMBRE_CLIENTE']
    TELEFONO_REFERENCIA=datos["TELEFONO_REFERENCIA_1"]
    nodo=datos["nodo"]
    troba=datos["troba"]
    Cmtsk=datos["Cmts"]
    from  t_test.models import Cmts, Nodo, Troba, Afectados

    for K in range(0,A-1):

         real_Fecha=Fecha[K]
         real_Hora=Hora[K]
         real_DURACION=DURACION[K]
         print(real_DURACION)
         real_CODIGO_CLIENTE=CODIGO_CLIENTE[K]
         real_NOMBRE_CLIENTE=NOMBRE_CLIENTE[K]
         real_TELEFONO_REFERENCIA=TELEFONO_REFERENCIA[K]
         print(real_TELEFONO_REFERENCIA)
         real_nodo=nodo[K]
         real_troba=troba[K]
         real_Cmts=Cmtsk[K]

         cmts1=Cmts.objects.get_or_create(cmtsNombre=real_Cmts)[0]
         nodo1=Nodo.objects.get_or_create(nodoNombre=real_nodo,cmts =cmts1)[0]
         troba1=Troba.objects.get_or_create(trobaNombre=real_troba,nodo=nodo1)[0]
         Afectados1=Afectados.objects.get_or_create(telefono=real_TELEFONO_REFERENCIA,
                                                    duracion=real_DURACION,hora=real_Hora,
                                                    fechaTrabajo=real_Fecha,codigoCliente=real_CODIGO_CLIENTE,
                                                    nombreCliente=real_NOMBRE_CLIENTE,troba=troba1)


if __name__ == '__main__':
    ctd=len(datos)
    Populate(ctd)
