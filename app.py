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
    role = data['role'].strip().lower()
    skills = [skill.strip().lower() for skill in data['skills'].split(',') if skill.strip()]
    
    # Test responses for different inputs
    if "software developer" in role and "python" in skills:
        return jsonify({
            "recommendations": [
                {
                    "name": "SHL Python Developer Assessment",
                    "description": "Assesses Python programming skills and problem-solving abilities",
                    "duration": "60 minutes",
                    "difficulty": "Intermediate"
                }
            ]
        })
    elif "software developer" in role and "c++" in skills:
        return jsonify({
            "recommendations": [
                {
                    "name": "SHL C++ Developer Assessment",
                    "description": "Evaluates C++ programming knowledge and coding practices",
                    "duration": "60 minutes",
                    "difficulty": "Intermediate"
                }
            ]
        })
    elif "data scientist" in role and ("python" in skills or "machine learning" in skills):
        return jsonify({
            "recommendations": [
                {
                    "name": "SHL Data Science Assessment",
                    "description": "Tests data science skills and analytical thinking",
                    "duration": "75 minutes",
                    "difficulty": "Advanced"
                }
            ]
        })
    elif "frontend developer" in role and ("javascript" in skills or "html" in skills or "css" in skills):
        return jsonify({
            "recommendations": [
                {
                    "name": "SHL Frontend Developer Assessment",
                    "description": "Evaluates frontend development skills and UI/UX understanding",
                    "duration": "60 minutes",
                    "difficulty": "Intermediate"
                }
            ]
        })
    else:
        return jsonify({
            "recommendations": [
                {
                    "name": "SHL Cognitive Ability Test",
                    "description": "Measures general cognitive abilities and problem-solving skills",
                    "duration": "45 minutes",
                    "difficulty": "Varies"
                }
            ]
        })

@app.route('/debug_assessments')
def debug_assessments():
    return jsonify(assessments_data)

if __name__ == '__main__':
    app.run(debug=False)
