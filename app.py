import json
from flask import Flask, render_template, request , jsonify
from bot import get_questions , get_answer 
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import DB_URI, APP_SECRET
from db import database,  ChatRecords, Question, Answer
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.secret_key = APP_SECRET
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    database.init_app(app)
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

@app.route('/')
def chat():
    # createQuetions()
    return render_template('index.html', questions=get_questions())

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
