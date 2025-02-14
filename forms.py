from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,EmailField

class UserForm(Form):
    matricula = StringField("Matricula")
    nombre = StringField("Nombre")
    apellido = StringField("Apellido")
    email = EmailField("Correo")
