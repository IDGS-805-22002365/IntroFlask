#Este archivo es en el que se trabajara
from flask import Flask

#Se crea la instancia de Flask esto es lo que se invoca para crear la aplicacion
app=Flask(__name__)

#Se crea la ruta/decorador principal
@app.route('/')
#Se crea la funcion que se ejecutara cuando se acceda a la ruta
def index():
    return 'Hola Mundo, hola'

@app.route('/adios')
def adios():
    return 'Adios Mundo'

#Se debe indicar desde donde se ejecutara la aplicacion
#El archivo que tenga este codigo sera el que ejecutara
if __name__ == '__main__':
    app.run(debug=True,port=8000)

#Para que la pagina se actualize con los cambios que se hacen aca se debe poner el comando debug=True
#Tambien se puede establecer el puerto en el que se ejecutara la aplicacion con el comando port=8000



