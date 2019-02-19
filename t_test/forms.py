import datetime
from django import forms
from .models import TareaNoc
from crispy_forms.helper import FormHelper
from django.contrib.admin import widgets
from bootstrap_datepicker_plus import DateTimePickerInput,TimePickerInput, DatePickerInput
from django import forms


responsables =(
        ('ArnoldV','Arnold Velasquez'),
        ('AdrianM','Adrian Martinez'),
        ('AlenjandroA','Alejandro  Alvarez')

)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class calendarioForm(forms.Form):

     date = forms.DateField(label='Ingrese la fecha a buscar',
         widget= DatePickerInput(format='%Y-%m-%d')
     )
class clienteForm(forms.Form):

     codigo = forms.IntegerField(label='Ingrese el codigo de cliente correspondiente',)

class nuevaTareaForm(forms.ModelForm):

    helper=FormHelper()
    helper.form_show_labels=True
    resumen=forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "5", }))
    responsable=forms.ChoiceField(widget=forms.Select, choices=responsables)

    class Meta():
        model=TareaNoc

        #fields='__all__'
        exclude = ('fechaFin',)
        localized_fields = '__all__'
        labels = {
            'remedy': 'Remedy ',
            'resumen' :  'Resumen',
            'fechaInicio' : 'Fecha de Inicio',
            'horaInicio' : 'Hora de Inicio',
            'horaFin' : 'Hora de Finalizacion',
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
             'horaInicio' : TimePickerInput(),
             'horaFin' : TimePickerInput(),



             }
