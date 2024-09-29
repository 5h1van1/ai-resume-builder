from flask import Flask, request, jsonify
import mysql.connector
import openai

app = Flask(__name__)  # Corrected __name__

# Set up the OpenAI API key (Replace with your actual OpenAI key)
openai.api_key = "your-openai-api-key"

# MySQL Database connection setup
db_config = {
    'user': 'root',          # Use your MySQL username
    'password': 'your-password',  # Use your MySQL password
    'host': 'localhost',
    'database': 'resume_builder'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Function to generate AI-powered resume content
def generate_ai_resume(full_name, experience, skills, job_description):
    prompt = f"Generate a resume for {full_name} based on the following experience, skills, and job description:\n\nExperience: {experience}\nSkills: {skills}\nJob Description: {job_description}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    resume_text = response.choices[0].text.strip()  # Fixed indentation
    return resume_text

# Endpoint to generate a resume
@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.json

    full_name = data['fullName']
    email = data['email']
    phone = data['phone']
    experience = data['experience']
    skills = data['skills']
    job_description = data['jobDescription']
    template = data['template']

    # Generate AI-powered resume content
    generated_resume = generate_ai_resume(full_name, experience, skills, job_description)

    # Skill gap feedback (mockup)
    feedback = f"Improve skills in leadership, advanced coding techniques based on the job requirements."

    # Insert data into the MySQL database
    connecti
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
from flask import Flask, request, jsonify
import mysql.connector
import openai
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS with your app

# Set up the OpenAI API key (Replace with your actual OpenAI key)
openai.api_key = "your-openai-api-key"

# MySQL Database connection setup
db_config = {
    'user': 'root',  # Use your MySQL username
    'password': 'your-password',  # Use your MySQL password
    'host': 'localhost',
    'database': 'resume_builder'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

# Function to generate AI-powered resume content
def generate_ai_resume(full_name, experience, skills, job_description):
    prompt = f"Generate a resume for {full_name} based on the following experience, skills, and job description:\n\nExperience: {experience}\nSkills: {skills}\nJob Description: {job_description}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    resume_text = response.choices[0].text.strip()
    return resume_text

# Endpoint to generate a resume
@app.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.json

    full_name = data['fullName']
    email = data['email']
    phone = data['phone']
    experience = data['experience']
    skills = data['skills']
    job_description = data['jobDescription']
    template = data['template']

    # Generate AI-powered resume content
    generated_resume = generate_ai_resume(full_name, experience, skills, job_description)

    # Skill gap feedback (mockup)
    feedback = f"Improve skills in leadership, advanced coding techniques based on the job requirements."

    # Insert data into the MySQL database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO resumes (full_name, email, phone, experience, skills, job_description, template, generated_resume, feedback)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (full_name, email, phone, experience, skills, job_description, template, generated_resume, feedback))

    connection.commit()
    cursor.close()
    connection.close()

    # Return the generated resume and feedback
    return jsonify({
        'resume': generated_resume,
        'feedback': feedback,
        'questions': [
            "Tell me about yourself.",
            "Why do you want this job?",
            "What are your strengths and weaknesses?",
            "Describe a challenge you've faced in a previous role."
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)
