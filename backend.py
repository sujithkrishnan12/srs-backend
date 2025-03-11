from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-srs', methods=['POST'])
def generate_srs():
    data = request.get_json()
    title = data.get('title')

    response = {
        'title': title,
        'message': 'SRS Generated Successfully'
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
