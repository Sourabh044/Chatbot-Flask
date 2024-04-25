from flask import Flask, render_template, request , jsonify
from bot import get_questions , get_answer 

app = Flask(__name__)


@app.route('/')
def chat():
    return render_template('index.html',questions=get_questions())


@app.route('/get-answer/',)
def response_answer():
    question = request.args.get('question')
    if not question or question == 0:
        return jsonify(list(get_questions()))
    # print(get_bot_response(question.lower()))
    answer,related_questions = get_answer(question)   
    return jsonify({
        'answer':answer,
        'related_questions':related_questions
    })

if __name__ == "__main__":
    app.run(debug=True,port=4100)