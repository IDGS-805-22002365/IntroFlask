
#Este archivo es en el que se trabajara
from flask import Flask , render_template


#Se crea la instancia de Flask esto es lo que se invoca para crear la aplicacion
app=Flask(__name__)

# #Se crea la ruta/decorador principal
# @app.route('/')
# #Se crea la funcion que se ejecutara cuando se acceda a la ruta
# def index():
#     return '<h1>Hola Mundo, hola</h1>'

@app.route('/user/<string:user>')
def user(user):
    return f'Hola {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'Numero: {n}'

@app.route('/user/<int:id>/<string:username>')
def username(id,username):
    return f"Usuario:{username}, con id:{id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default")
@app.route("/default/<string:tem>")
def funcion1(tem="Juan"):
    return f"Hola {tem}"

@app.route('/adios')
def adios():
    return 'Adios Mundo'

@app.route("/formulario")
def form1():
    return """
            <form>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre">
            <label for="apellido">Apellido:</label>
            <input type="text" id="apellido" name="apellido">
            </form>
            """

@app.route("/")
def index1():
    titulo="IDGS805"
    lista=["Python","Java","C#","JavaScript"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

#Se debe indicar desde donde se ejecutara la aplicacion
#El archivo que tenga este codigo sera el que ejecutara
if __name__ == '__main__':
    app.run(debug=True,port=8000)

#Para que la pagina se actualize con los cambios que se hacen aca se debe poner el comando debug=True
#Tambien se puede establecer el puerto en el que se ejecutara la aplicacion con el comando port=8000
