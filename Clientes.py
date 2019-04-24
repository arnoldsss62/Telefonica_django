import pandas as pd

#cARGA EL EXCEL DE GPON con nombre gpon_cierre
datos = pd.read_excel('gpon_cierre.xlsx')

datos_codigo=datos['CLIENTE']
listaindices=list(datos_codigo.index.values)
datos_cmts=datos['CMTS']
datos_nodo=datos['NODO']
datos_troba=datos['PLANO']
datos_Nombre=datos['NOMBRE']
datos_apellidoPA=datos['APE_PAT']
datos_apellidoMA=datos['APE_MAT']
datos_servicio=datos['TIPOPERU8K']

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")

import django

django.setup()

import random
from  t_test.models import Cmts, Nodo, Troba, Usuario
import numpy as np
from django.conf import settings
from django.utils.timezone import make_aware

django.setup()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR= os.path.join(BASE_DIR,'Telefonica_django/media')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")

def Populate(A):
    for K in range(0,A-1):
         print (K)
         N=listaindices[K]

         real_cmtsNombre=datos_cmts[K]
         real_nodoNombre=datos_nodo[K]
         real_trobaNombre=datos_troba[K]
         real_codigo=datos_codigo[K]
         real_Nombre=datos_Nombre[K]
         PA=datos_apellidoPA[K]
         MA=datos_apellidoMA[K]
         if isinstance(PA,str) and isinstance(MA,str):
            datos_apellido=PA + MA
         if isinstance(PA,str) and isinstance(MA,float):
            datos_apellido=PA + str(MA)
         if isinstance(PA,float) and isinstance(MA,str):
            datos_apellido=str(PA) + MA
         if isinstance(PA,float) and isinstance(MA,float):
            datos_apellido=str(PA) + str(MA)
         real_Apellido=datos_apellido
         real_servicio=datos_servicio[K]

         cmts1=Cmts.objects.get_or_create(cmtsNombre=real_cmtsNombre)[0]
         nodo1=Nodo.objects.get_or_create(nodoNombre=real_nodoNombre,cmts =cmts1)[0]
         troba1=Troba.objects.get_or_create(trobaNombre=real_trobaNombre,nodo=nodo1)[0]
         Usuario1=Usuario.objects.get_or_create(servicio=real_servicio,nombre=real_Apellido,apellido=real_Apellido,codigoCliente=real_codigo,troba=troba1)

if __name__ == '__main__':

    cd=len(datos)
    Populate(cd)
