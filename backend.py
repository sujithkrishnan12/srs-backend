from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/generate-srs', methods=['POST'])
def generate_srs():
    data = request.json
    project_name = data.get('projectName', '')
    description = data.get('description', '')

    # Generate the SRS Text
    srs_text = f"SRS Document for {project_name}\n\nDescription:\n{description}"
    
    # Return the SRS Text as JSON response
    return jsonify({'srsText': srs_text})

if __name__ == '__main__':
    app.run(debug=True)
