from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load assessments from JSON file
def load_assessments():
    try:
        with open('assessments.json', 'r') as file:
            return json.load(file)['assessments']
    except FileNotFoundError:
        return {}

SAMPLE_ASSESSMENTS = load_assessments()

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    role = data['role']
    skills = data['skills'] if isinstance(data['skills'], list) else data['skills'].split(',')

    recommendations = []
    for assessment in SAMPLE_ASSESSMENTS.values():
        if role.lower() in assessment['role'].lower():
            if any(skill.lower() in [s.lower() for s in assessment['skills']] for skill in skills):
                recommendations.append(assessment)
    
    if not recommendations:
        # If no specific recommendations, suggest cognitive test
        recommendations.append(SAMPLE_ASSESSMENTS.get('cognitive', {}))

    return jsonify({'recommendations': recommendations})

@app.route('/api/search', methods=['GET'])
def search_assessments():
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({
            'error': 'Please provide a search query',
            'status': 400
        }), 400
    
    results = []
    for assessment in SAMPLE_ASSESSMENTS.values():
        if (query in assessment['title'].lower() or 
            query in assessment['description'].lower() or 
            any(query in skill.lower() for skill in assessment['skills'])):
            results.append(assessment)
    
    return jsonify({
        'query': query,
        'results': results,
        'count': len(results)
    })

if __name__ == '__main__':
    app.run(debug=True)
