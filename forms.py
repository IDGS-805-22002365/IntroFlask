from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,EmailField
from wtforms import validators,RadioField

class UserForm(Form):
    matricula = StringField("Matricula",[
        validators.data_required(message="Favor de ingresar la matricula"),
        validators.length(min=3,max=10,message="La matricula debe tener entre 3 y 10 caracteres")
    ])
    nombre = StringField("Nombre",[
        validators.data_required(message="Favor de ingresar el nombre")
    ])
    apellido = StringField("Apellido",[
        validators.data_required(message="Favor de ingresar el apellido")
    ])
    email = EmailField("Correo",[
        validators.Email(message="Favor de ingresar un correo valido")
    ])


class Zodiaco(FlaskForm):
    nombre = StringField("Nombre", [
        validators.data_required(message="Favor de ingresar el nombre")
    ])
    aPaterno = StringField("Apellido Paterno", [
        validators.data_required(message="Favor de ingresar el apellido paterno")
    ])
    aMaterno = StringField("Apellido Materno", [
        validators.data_required(message="Favor de ingresar el apellido materno")
    ])
    dia = IntegerField("Día", [
        validators.NumberRange(min=1, max=31, message="Día inválido"),
        validators.data_required(message="Favor de ingresar un día válido")
    ])
    mes = IntegerField("Mes", [
        validators.NumberRange(min=1, max=12, message="Mes inválido"),
        validators.data_required(message="Favor de ingresar un mes válido")
    ])
    anio = IntegerField("Año", [
        validators.NumberRange(min=1900, max=2100, message="Año inválido"),
        validators.data_required(message="Favor de ingresar un año válido")
    ]) 
    sexo = RadioField("Sexo", choices=[("M", "Masculino"), ("F", "Femenino")], default="M")
