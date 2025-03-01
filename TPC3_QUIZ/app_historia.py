# Backend & Frontend: app.py (Flask with Jinja templates)
from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_cors import CORS
import random
from gen_questions import generate_questions
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
CORS(app)

def shuffle_list(value):
    temp_list = list(value)
    random.shuffle(temp_list)
    return temp_list

app.jinja_env.filters['shuffle'] = shuffle_list

TOTAL_QUESTIONS = 6 

@app.route('/')
def home():
    session['score'] = 0
    session['questions_answered'] = 0
    global test_questions
    test_questions = generate_questions(TOTAL_QUESTIONS)
    random.shuffle(test_questions)
    session['questions'] = test_questions
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        question_text = request.form.get('question')
        current_question = session.get('current_question')
        
        if current_question and current_question['question'] == question_text:
            correct_pairs = []
            correct_answer = None
            if "pairs" in current_question:
                # Handle correspond question
                user_pairs = request.form.get('pairs')
                if user_pairs:
                    user_pairs = json.loads(user_pairs)  # Parse the JSON string
                    user_pairs = [tuple(pair) for pair in user_pairs]  # Convert to list of tuples
                else:
                    user_pairs = []
                correct_pairs = current_question['pairs']
                correct_answer = correct_pairs
                correct = sorted(user_pairs) == sorted(correct_pairs)
                attempted_answer = user_pairs
            else:
                # Handle multiple choice question
                correct = current_question['answer'] == user_answer
                correct_answer = current_question['answer']
                attempted_answer = user_answer
            
            session['score'] = session.get('score', 0) + (1 if correct else 0)
            session['questions_answered'] = session.get('questions_answered', 0) + 1
            
            if session['questions_answered'] >= TOTAL_QUESTIONS:
                return render_template('result.html', correct=correct, correct_answer=correct_answer, attempted_answer=attempted_answer, score=session['score'], final=True, total_questions=TOTAL_QUESTIONS)
            
            return render_template('result.html', correct=correct, correct_answer=correct_answer, attempted_answer=attempted_answer, score=session['score'], final=False, total_questions=TOTAL_QUESTIONS)
    
    if 'questions' not in session or not session['questions']:
        return redirect(url_for('home'))
    
    question = session['questions'].pop(0)
    session['current_question'] = question  # Store the current question in the session
    question_number = session.get('questions_answered', 0) + 1
    if "pairs" in question:
        return render_template('correspond.html', question=question, question_number=question_number, total_questions=TOTAL_QUESTIONS)
    else:
        return render_template('quiz.html', question=question, question_number=question_number, total_questions=TOTAL_QUESTIONS)

@app.route('/score')
def score():
    session['questions_answered'] = 0  # Reset the question number
    return render_template('score.html', score=session.get('score', 0), total_questions=TOTAL_QUESTIONS)

app.template_folder = 'templates'

if __name__ == '__main__':
    app.run(debug=True)
