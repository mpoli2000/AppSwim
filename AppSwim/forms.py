from django import forms

class Form_Nadador(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    edad = forms.IntegerField()

class Form_Profesor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class Form_Estilo(forms.Form):
    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=200)

class Form_Slot(forms.Form):
    fecha = forms.DateField()
    horario = forms.TimeField()
    duracion = forms.IntegerField()