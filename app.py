from flask import Flask,request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression')
        
        # Utilisation de eval pour calculer l'expression
        result = eval(expression)  # Attention à l'utilisation de eval()
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, port=5001)

