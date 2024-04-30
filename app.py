import json
from flask import Flask, render_template, request , jsonify
from bot import get_questions
from config import Development
from db import database,  ChatRecords, Question
from routes import auth_bp
from flask_login import login_required
from auth import login_manager, migrate, bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Development)
    database.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, database)
    bcrypt.init_app(app)
    return app

app = create_app()


def save_chat_record(question, answer, user_id):
    chat_record = ChatRecords(
        question=question, answer=answer, user_id=user_id)
    database.session.add(chat_record)
    database.session.commit()
    return True


app.register_blueprint(auth_bp)

@app.route('/')
@login_required
def chat():
    return render_template('chat.html', questions=get_questions())

@app.route('/get-answer/',)
def response_answer():
    question = request.args.get('question')
    question_obj = Question.query.filter_by(text=question).all()
    if question_obj:
        user_id = request.args.get('user_id', 1)
        answer = question_obj[0].answers[0].text
        related_questions = [
            q.related_question.text for q in question_obj[0].related_questions]
        save_chat_record(question, answer, user_id)
        return jsonify({
            'answer': answer,
            'related_questions': related_questions
        })
    if not question_obj or question == 0:
        return jsonify(get_questions())


def createQuetions():
    with open('data.json') as f:
        data = json.load(f)
        for q in data.keys():
            question = Question(text=q)
            database.session.add(question)

    database.session.commit()


if __name__ == "__main__":
    app.run(debug=True, port=4100)
