import datetime
from django import forms
from .models import TareaNoc
from crispy_forms.helper import FormHelper
from django.contrib.admin import widgets
from bootstrap_datepicker_plus import DateTimePickerInput,TimePickerInput

class nuevaTareaForm(forms.ModelForm):

    helper=FormHelper()
    helper.form_show_labels=True

    class Meta():
        model=TareaNoc

        #fields='__all__'
        exclude = ('fechaHoraFin',)
        localized_fields = '__all__'
        labels = {
            'remedy': 'Remedy ',
            'resumen' :  'Resumen',
            'fechaHoraInicio': 'Fecha de Inicio',
            #'fechaHoraFin': 'Fecha de Finalizacion',
            'responsable' : 'Responsable',
            'elementoRed' : 'Elemento de Red',
            'region' : 'Region',
            'impacto' : 'Impacto',
            'servAfectados' : 'Servicios afectados',
            'descripccionNoTecnica' : 'Descripccion no Tecnica',
            'proyecto_beneficio' : 'Proyecto/Beneficios',
            'tiempoRollback' : 'Tiempo de Rollback',

        }

        help_texts = {
            'remedy': 'Numero de ticket ',
            'resumen' :  'Resumen',
            'fechaHoraInicio': 'YYYY:MM:DD',
            'responsable' : 'Nombre de la personsa a cargo',
        }
        widgets = {
             'fechaHoraInicio': DateTimePickerInput(format='%Y-%m-%d %H:%M:%S'), # specify date-time-frmatç
             'tiempoRollback': TimePickerInput(),
         }
