from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('new.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    role = data['role']
    skills = data['skills'] if isinstance(data['skills'], list) else data['skills'].split(',')

    recommendations = []
    if role.lower() == "software developer":
        if "Python" in skills:
            recommendations.append("Take SHL Python Developer Assessment")
        if "C++" in skills:
            recommendations.append("Take SHL C++ Developer Assessment")
        if not recommendations:
            recommendations.append("Try SHL Cognitive Ability Test")

    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
