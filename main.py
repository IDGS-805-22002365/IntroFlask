from flask import Flask, render_template, request

# Se crea la instancia de Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def index1():
    titulo = "IDGS805"
    lista = ["Python", "Java", "C#", "JavaScript"]
    return render_template("index.html", titulo=titulo, lista=lista)

# Rutas con parámetros dinámicos
@app.route('/user/<string:user>')
def user(user):
    return f'Hola {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'Numero: {n}'

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f"Usuario: {username}, con id: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"La suma es: {n1 + n2}"

@app.route("/default")
@app.route("/default/<string:tem>")
def funcion1(tem="Juan"):
    return f"Hola {tem}"

@app.route('/adios')
def adios():
    return 'Adios Mundo'

# Rutas de formularios
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

# Rutas de operaciones matemáticas
@app.route("/operaciones")
def operaciones():
    return render_template("OperasBas.html")

@app.route("/resultado", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")  # Obtiene el valor de n1
        num2 = request.form.get("n2")  # Obtiene el valor de n2
        return f"La multiplicación de {num1} x {num2} es: {int(num1) * int(num2)}"
    return "Método no permitido"

@app.route("/resultado2", methods=["GET", "POST"])
def result2():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if not num1 or not num2 or not operacion:
            return "Por favor, completa todos los campos y selecciona una operación."

        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return "Por favor, ingresa números válidos."
        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2
        elif operacion == "division":
            if num2 == 0:
                return "No se puede dividir por cero."
            resultado = num1 / num2
        else:
            return "Operación no válida"
        # Pasar el resultado y la operación a la plantilla
        return render_template("OperasBas.html", resultado=resultado, operacion=operacion)
    return render_template("OperasBas.html")

# Rutas de plantillas adicionales
@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

# rutas para cinepolis
@app.route("/cinepolis1")
def cinepolis1():
    return render_template("cinepolis1.html")

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=8000)