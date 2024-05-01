from flask import render_template,  Blueprint, request
from db import Question

questions_bp = Blueprint('questions', __name__, url_prefix='questions/')


@questions_bp.route('/create/', methods=['GET', 'POST'])
def create_questions():
    if request.method == 'POST':
        data = request.form
        question = Question(data['question'], data['answer'],)
    return render_template('admin/add_question.html')
