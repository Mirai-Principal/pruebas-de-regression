from flask import Flask, render_template, request
import math  # Para usar sqrt y potencias

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora</title>
    </head>
    <body>
        <h1>Calculadora Básica</h1>
        <form method="post" action="/calcular">
            <input type="number" id="number1" name="num1" placeholder="Número 1" required>
            <input type="number" id="number2" name="num2" placeholder="Número 2" required>
            <select id="operation" name="operation" required>
                <option value="suma">Suma</option>
                <option value="resta">Resta</option>
                <option value="multiplicacion">Multiplicación</option>
                <option value="division">División</option>
                <option value="raiz">Raíz Cuadrada (Número 1)</option>
                <option value="potencia">Potencia (Número 1 ^ Número 2)</option>
            </select>
            <button type="submit">Calcular</button>
        </form>
    </body>
    </html>
    """

@app.route("/calcular", methods=["POST"])
def calcular():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "suma":
            resultado = num1 + num2
        elif operation == "resta":
            resultado = num1 - num2
        elif operation == "multiplicacion":
            resultado = num1 * num2
        elif operation == "division":
            if num2 == 0:
                return "Error: No se puede dividir entre cero."
            resultado = num1 / num2
        elif operation == "raiz":
            if num1 < 0:
                return "Error: No se puede calcular la raíz cuadrada de un número negativo."
            resultado = math.sqrt(num1)
        elif operation == "potencia":
            resultado = math.pow(num1, num2)
        else:
            return "Operación no válida."

        return f"El resultado es: {resultado}"
    except ValueError:
        return "Error: Entrada no válida."

if __name__ == "__main__":
    app.run(debug=True)
