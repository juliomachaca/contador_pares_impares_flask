from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta principal para mostrar la interfaz
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el conteo de pares e impares
@app.route('/contar', methods=['POST'])
def contar_pares_impares():
    try:
        # Obtener los números desde la solicitud POST
        numeros = request.json.get('numeros', [])
        pares = sum(1 for num in numeros if num % 2 == 0)
        impares = sum(1 for num in numeros if num % 2 != 0)

        # Devolver los resultados en formato JSON
        return jsonify({'pares': pares, 'impares': impares})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
