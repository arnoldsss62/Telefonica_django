import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "telefonica_test.settings")

import django

django.setup()

#fake script

import random
from  t_test.models import Cmts, Nodo, Troba, Usuario, InfoPlanta, InfoCore, TareaProgramada
from faker import Faker
from random import randrange,choice
import datetime
import radar
import csv
import numpy as np

fakegen= Faker()

def Populate(N=5):
    for _ in range(N):

         fake_cmtsNombre=choice(['VILLA EL SALVADOR1','SAN JUAN4','1EROMAYO1','CHORRILLOS1','MAGDALENA2','MAGDALENA1','SAN JUAN1','SAN JUAN2','SAN JUAN3'])
         fake_nodoNombre=choice(['CA','CU','CV','LC','LF','LM','LO','MA','MI','P3','PI','RA','RO','SB','SI','SV','T1','VI','WA'])
         fake_trobaNombre= 'R'+ str(randrange(100,105))
         fake_nombre= choice(['Jhon','Sansa','Tyron','Aria','Brie','Bran','Ned','Rob','Robet','Summer','Ghost','Lady','Cathelyn'])
         fake_apellido=choice(['Dominguez','Lu','Ra','Zen','Brian','Tarth','Snow','Sand','Targaryen','Stark','Lannister','Black Fire'])
         fake_codigoCliente=randrange(100000, 9999999)
         fake_remedy='CRQ0000'+ str(randrange(393881,399999))
         fake_estado=choice(['Cerrado', 'Abierto'])
         fake_corteS_N=choice(['True','False'])
         fake_tipoTrabajo=choice(["PARTICION_OPTICA","ACONDICIONAR_FUENTE_DE_ENERGIA","CONEXIONADO_DE_DISPOSITIVOS","PARTICION_COAXIAL","CONEXIONADO","CAMBIO_DE_TROBA","TRABAJO_DE_EMERGENCIA"])
         fake_remitente=choice(['Jhon','Sansa','Tyron','Aria','Brie','Bran','Ned','Rob','Robet','Summer','Ghost','Lady','Cathelyn'])
         fake_grupoCoordinador=choice(['Busqueda y saneamiento','Capacidad y procesos','Energia','Huaweia','Ingenieria Core IP','Ingenieria de Datos','Ingenieria Facilities','metro y Backhaul','Transporte'])
         fake_riesgo=choice(['1','2','3','4','5'])
         fake_site=choice(['San Borja','Carhuacoto','La Victoria','Lince','Cedros','Urubamba','Huancas','Tuman_Ura','San Juan','Higuereta'])
         fake_fechaInicio=radar.random_date(start='2019-02-05', stop='2019-02-12')
         fake_fechaFin=radar.random_date(start='2019-03-10', stop='2019-05-18')

         cmts1=Cmts.objects.get_or_create(cmtsNombre=fake_cmtsNombre)[0]
         nodo1=Nodo.objects.get_or_create(nodoNombre=fake_nodoNombre,cmts =cmts1)[0]
         troba1=Troba.objects.get_or_create(trobaNombre=fake_trobaNombre,nodo=nodo1)[0]
         infoPlanta1=InfoPlanta.objects.get_or_create(remedy=fake_remedy,estado=fake_estado,corteS_N=fake_corteS_N,tipoTrabajo=fake_tipoTrabajo,troba=troba1)[0]
         infoCore1=InfoCore.objects.get_or_create(remedy=fake_remedy,remitente=fake_remitente,grupoCoordinador=fake_grupoCoordinador,riesgo=fake_riesgo,site=fake_site,cmts=cmts1)[0]
         tareaProgramada=TareaProgramada.objects.get_or_create(fechaInicio=fake_fechaInicio,fechaFin=fake_fechaFin,infoCore=infoCore1,infoPlanta=infoPlanta1)
         usuario=Usuario.objects.get_or_create(nombre=fake_nombre,apellido=fake_apellido,codigoCliente=fake_codigoCliente,troba=troba1)


if __name__ == '__main__':

    print('Populando la DB')
    Populate(100)
