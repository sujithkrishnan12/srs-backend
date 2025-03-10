from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from fpdf import FPDF
import os

app = Flask(__name__)
CORS(app)

# ✅ Generate SRS PDF Function
def generate_srs_pdf(project_name, description, requirements):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # ✅ Add Title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, txt=f"SRS Document - {project_name}", ln=True, align='C')

    # ✅ Add Project Name
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="1. Project Name:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=project_name)

    # ✅ Add Description
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="2. Project Description:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=description)

    # ✅ Add Functional Requirements
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt="3. Functional Requirements:", ln=True)
    pdf.set_font("Arial", size=12)
    for req in requirements:
        pdf.cell(200, 10, txt=f"- {req}", ln=True)

    # ✅ Save PDF to a File
    pdf_path = "srs.pdf"
    pdf.output(pdf_path)
    return pdf_path

# ✅ API to Generate SRS
@app.route('/generate-srs', methods=['POST'])
def generate_srs():
    # ✅ Get Data from React Form
    data = request.get_json()
    project_name = data.get('project_name')
    description = data.get('description')
    requirements = data.get('requirements')

    # ✅ Generate PDF
    pdf_path = generate_srs_pdf(project_name, description, requirements)

    # ✅ Send PDF Back to React
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
