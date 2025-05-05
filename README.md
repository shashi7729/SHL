# SHL
Recommended Assessments
# SHL Assessment Recommender

## Problem Statement
Create a web application that recommends appropriate SHL assessments based on a user's role and skills.

## Solution Approach

### 1. Architecture
- **Frontend**: HTML/CSS/JavaScript single-page application
- **Backend**: Flask Python server
- **Data Storage**: JSON file for assessment data

### 2. Key Components

#### Data Structure (`assessments.json`)
- Structured JSON format for assessment data
- Each assessment contains:
  - ID, name, role, required skills
  - Description, duration, difficulty level

#### Backend (`app.py`)
- Flask server with two endpoints:
  - `/`: Serves the main page
  - `/recommend`: API endpoint for recommendations
- Recommendation logic:
  - Matches user's role and skills with assessments
  - Returns detailed assessment information
  - Falls back to cognitive test if no matches found

#### Frontend (`project.html`)
- Clean, responsive UI with modern design
- Form for role and skills input
- Dynamic display of recommendations
- Real-time updates without page refresh

### 3. Features
- Role-based assessment matching
- Skill-based filtering
- Detailed assessment information display
- Responsive design with animations
- Error handling and fallback recommendations

### 4. Technical Implementation
- RESTful API design
- Asynchronous frontend-backend communication
- Case-insensitive matching for better user experience
- Modular data structure for easy updates
### 5. Now you can test different inputs and get different recommendations:
For Python Developer:
Role: Software Developer
Skills: Python
You'll get: SHL Python Developer Assessment
For C++ Developer:
Role: Software Developer
Skills: C++
You'll get: SHL C++ Developer Assessment
For Data Scientist:
Role: Data Scientist
Skills: Python, Machine Learning
You'll get: SHL Data Science Assessment
For Frontend Developer:
Role: Frontend Developer
Skills: JavaScript, HTML, CSS
You'll get: SHL Frontend Developer Assessment
For Other Roles/Skills:
Role: Manager
Skills: Leadership
You'll get: SHL Cognitive Ability Test

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run server: `python app.py`
3. Access application at: `http://localhost:5000`
4. run in web browser http://127.0.0.1:5000/
   
