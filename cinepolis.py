from flask import Flask, render_template, request

app = Flask(__name__)

class Boleto:
    def __init__(self):
        self.boletosPorPersona = 7
        self.precioBoleto = 12.00

    def calcular_total(self, grupoPersonas, numBoletos, tarjeta_cienco):
        if numBoletos > grupoPersonas * self.boletosPorPersona:
            return None, "No se pueden comprar más de 7 boletos por persona.\n¿Deseas modificar el número de personas o boletos?"

        total = numBoletos * self.precioBoleto
        if numBoletos > 5:
            total *= 0.85  # 15% de descuento
        elif 3 <= numBoletos <= 5:
            total *= 0.90  # 10% de descuento
        
        if tarjeta_cienco:
            total *= 0.90  # 10% adicional por tarjeta CIENCO
        
        return round(total, 2), None

lista_personas = []

@app.route("/", methods=["GET", "POST"])
def cinepolis1():
    total_pagar = None
    mensaje = None
    mostrar_ticket = False
    
    if request.method == "POST":
        if "cancelar" in request.form:
            return render_template("cinepolis.html", total_pagar=None, mensaje=None, mostrar_ticket=False, lista_personas=lista_personas)

        nombre = request.form["nombre"]
        grupoPersonas = int(request.form["grupoPersonas"])
        numBoletos = int(request.form["numBoletos"])
        tarjeta_cienco = request.form["cineco"] == "si"

        sistema = Boleto()
        total_pagar, mensaje = sistema.calcular_total(grupoPersonas, numBoletos, tarjeta_cienco)

        if mensaje:
            return render_template("cinepolis.html", mensaje=mensaje, total_pagar=None, mostrar_ticket=False, lista_personas=lista_personas)
        
        lista_personas.append({"nombre": nombre, "total": total_pagar})
        mostrar_ticket = True
    
    total_general = sum(p["total"] for p in lista_personas)
    return render_template("cinepolis.html", total_pagar=total_pagar, mensaje=mensaje, mostrar_ticket=mostrar_ticket, lista_personas=lista_personas, total_general=total_general)

if __name__ == "__main__":
    app.run(debug=True)
