from django.db import models
#Author: Arnold Velasquez  Ortiz

# Create your models here.

class Cmts(models.Model):
    cmtsId=models.AutoField(primary_key=True)
    cmtsNombre=models.CharField(max_length=20)# No usar jefatura xd, aqui va relacion de jose veliz

    def __str__(self):
        return self.cmtsNombre


class Nodo(models.Model):
    nodoId=models.AutoField(primary_key=True)
    nodoNombre=models.CharField(max_length=20)
    cmts=models.ForeignKey(Cmts,on_delete=models.CASCADE, default='N0')


    def __str__(self):
        return self.nodoNombre

class Troba(models.Model):
    trobaId=models.AutoField(primary_key=True)
    trobaNombre=models.CharField(max_length=20)
    nodo=models.ForeignKey(Nodo,on_delete=models.CASCADE)

    def __str__(self):
        return self.trobaNombre


class Usuario(models.Model):
    usuarioId=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=80)
    codigoCliente=models.IntegerField()
    troba=models.ForeignKey(Troba,on_delete=models.CASCADE)
    #telefono1=models.CharField(max_length=10)
    #telefono2=models.charfield(max_length=10)
    def __str__(self):
        return self.nombre


class InfoPlanta(models.Model):
    infoPlantaId=models.AutoField(primary_key=True)
    remedy=models.CharField(max_length=100)
    estado=models.CharField(max_length=45)
    corteS_N=models.CharField(max_length=10)
    tipoTrabajo=models.CharField(max_length=45)
    site=models.CharField(max_length=45)#solo para rellenar :v
    troba=models.ForeignKey(Troba,on_delete=models.CASCADE)

    def __str__(self):
        return self.remedy


class InfoCore(models.Model):
    infoCoreId=models.AutoField(primary_key=True)
    remedy=models.CharField(max_length=100)
    remitente=models.CharField(max_length=45)
    grupoCoordinador=models.CharField(max_length=45)
    riesgo=models.SmallIntegerField()
    site=models.CharField(max_length=45)#zona para mostrar a la area comercial y asociar a los CMTS, inexacto
    #cmts=models.ForeignKey(Cmts,on_delete=models.CASCADE)

    def __str__(self):
        return self.remedy


class TareaProgramada(models.Model):
    tareaProgramadaId=models.AutoField(primary_key=True)
    fecha=models.DateField()
    horaInicio=models.TimeField(max_length=10)
    horaFin=models.TimeField(max_length=10)
    infoCore=models.ForeignKey(InfoCore,on_delete=models.CASCADE,blank=True, null=True)
    infoPlanta=models.ForeignKey(InfoPlanta,on_delete=models.CASCADE,blank=True, null=True)
    area=models.CharField(max_length=10)

    def __str__(self):
        return 'tarea programada %s' % self.tareaProgramadaId


#Modelo creado para cubrir parte de trabajo requerido por la Gestion de Cambios
class TareaNoc(models.Model):
    #Este es el id del cambio
    remedy=models.CharField(max_length=60)
    resumen=models.CharField(max_length=100)
    fechaInicio=models.DateField()
    horaInicio=models.TimeField(max_length=10)
    fechaFin=models.DateField(auto_now_add=True, blank=True)
    horaFin=models.TimeField(max_length=10, blank=True,null=True)
    responsable=models.CharField(max_length=60)
    elementoRed=models.CharField(max_length=60)
    region=models.CharField(max_length=60)
    impacto=models.CharField(max_length=2000)
    servAfectados=models.CharField(max_length=60)
    descripccionNoTecnica=models.CharField(max_length=2000)
    proyecto_beneficio=models.CharField(max_length=100)
    tiempoRollback=models.TimeField(max_length=200, blank=True, null=True)

class Afectados(models.Model):
    afectadoId=models.AutoField(primary_key=True)
    nombreCliente=models.CharField(max_length=200)
    codigoCliente=models.CharField(max_length= 200)
    troba=models.ForeignKey(Troba,on_delete=models.CASCADE)
    fechaTrabajo=models.DateField(max_length = 200 )
    hora=models.TimeField(max_length=10)
    duracion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)