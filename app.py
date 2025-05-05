# app.py
from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load assessments data
with open('assessments.json', 'r') as f:
    assessments_data = json.load(f)

@app.route('/')
def index():
    return render_template('project.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    role = data['role'].lower()
    skills = [skill.strip().lower() for skill in data['skills'].split(',')]

    recommendations = []
    
    # Find matching assessments
    for assessment in assessments_data['assessments']:
        # Check if role matches
        if role in assessment['role'].lower():
            # Check if user has required skills
            required_skills = [skill.lower() for skill in assessment['required_skills']]
            if not required_skills or any(skill in skills for skill in required_skills):
                recommendations.append({
                    'name': assessment['name'],
                    'description': assessment['description'],
                    'duration': assessment['duration'],
                    'difficulty': assessment['difficulty']
                })

    # If no specific recommendations, suggest cognitive test
    if not recommendations:
        cognitive_test = next(a for a in assessments_data['assessments'] if a['id'] == 'cognitive')
        recommendations.append({
            'name': cognitive_test['name'],
            'description': cognitive_test['description'],
            'duration': cognitive_test['duration'],
            'difficulty': cognitive_test['difficulty']
        })

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=False)
