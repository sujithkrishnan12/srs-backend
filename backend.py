from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate-srs', methods=['POST'])
def generate_srs():
    data = request.get_json()

    title = data.get('title', 'Untitled Project')
    description = data.get('description', 'No description provided.')
    modules = data.get('modules', [])

    srs_content = f"""
    # Software Requirements Specification (SRS)

    ## 1. Introduction
    **Project Title:** {title}
    **Description:** {description}

    ## 2. Functional Requirements
    """

    if 'Expense Tracking' in modules:
        srs_content += """
        ### Expense Tracking
        - Track daily, weekly, and monthly expenses.
        - Generate expense reports.
        - Categorize expenses into food, travel, bills, etc.
        """

    if 'Budget Management' in modules:
        srs_content += """
        ### Budget Management
        - Set monthly or annual budgets.
        - Receive alerts when approaching budget limits.
        - Generate budget summary reports.
        """

    if 'Bill Reminders' in modules:
        srs_content += """
        ### Bill Reminders
        - Set reminders for due bills.
        - Send email/SMS notifications for upcoming bills.
        - Generate a bill payment history.
        """

    if 'Investment Advice' in modules:
        srs_content += """
        ### Investment Advice
        - Provide personalized investment advice.
        - Track stock market trends.
        - Recommend savings and investment plans.
        """

    srs_content += """
    ## 3. Non-Functional Requirements
    - The system should be user-friendly and easy to navigate.
    - High-level security for user financial data.
    - Scalable to handle large volumes of data.
    """

    return jsonify({'srs': srs_content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
