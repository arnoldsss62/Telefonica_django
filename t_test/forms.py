import datetime
from django import forms
from .models import TareaNoc
from crispy_forms.helper import FormHelper
from django.contrib.admin import widgets
from bootstrap_datepicker_plus import DateTimePickerInput,TimePickerInput, DatePickerInput
from django import forms


class calendarioForm(forms.Form):

     date = forms.DateField(label='Ingrese la fecha a buscar',
         widget= DatePickerInput(format='%Y-%m-%d')
     )

class nuevaTareaForm(forms.ModelForm):

    helper=FormHelper()
    helper.form_show_labels=True

    class Meta():
        model=TareaNoc

        #fields='__all__'
        exclude = ('fechaFin',)
        localized_fields = '__all__'
        labels = {
            'remedy': 'Remedy ',
            'resumen' :  'Resumen',
            'fechaInicio' : 'Fecha de Inicio',
            'HoraInicio' : 'Hora de Inicio',
            'HoraFin' : 'Hora de Finalizacion',
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
            'fechaInicio': 'YYYY:MM:DD',
            'responsable' : 'Nombre de la personsa a cargo',
        }
        widgets = {
             'fechaInicio': DatePickerInput(format='%Y-%m-%d '), # specify date-time-frmatç
             'tiempoRollback': TimePickerInput(),
             'HoraInicio' : TimePickerInput(),
             'HoraFin' : TimePickerInput(),



             }
