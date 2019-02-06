from django.urls import path,re_path
from t_test import views

#TEMPLATE TAG IMPORTANTE

app_name="t_test"

urlpatterns = [

    path('usuarios/<int:id>',views.usuarios,name='usuarios'),
    path('add',views.addTarea,name='formulario')

]
