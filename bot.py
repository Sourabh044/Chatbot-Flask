# Dictionary to store questions, answers, and related questions
import json

with open('data.json', 'r') as data:
    qa_data = json.load(data)

# Function to display the available questions
def show_questions() -> None:
    print("Available Questions:")
    for question in qa_data.keys():
        print("- " + question)


# Function to get the questions
def get_questions():
    return qa_data.keys()


# Function to get the user's answer and provide feedback
def get_answer(question: str) -> (tuple[None, None] | tuple):
    try:
        answer, related_questions = qa_data[question]
    except KeyError:
        print("Invalid question. Please try again.")
        return None, None
    return answer , related_questions


if __name__ == "__main__":
    # Main loop
    print("Welcome to the Question-Answer Bot!")
    while True:
        show_questions()
        question = input("Enter a question (or 'quit' to exit): ")
        if question.lower() == "quit":
            break
        if question in qa_data:
            get_answer(question)
        else:
            print("Invalid question. Please try again.")