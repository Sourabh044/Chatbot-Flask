# Dictionary to store questions, answers, and related questions
qa_data = {
    "Hi": ["Hello",[]],
    "What is the capital of France?": ["Paris", ["What is the currency of France?", "What is the population of Paris?"]],
    "What is the largest ocean on Earth?": ["Pacific Ocean", ["What is the deepest point in the Pacific Ocean?"]],
    "Who is the author of the Harry Potter series?": ["J.K. Rowling", ["How many Harry Potter books are there?"]],
    "What is the smallest planet in our solar system?": ["Mercury", ["What is the temperature range on Mercury?"]],
    "What is the currency of France?": ["Euro", []],
    "What is the population of Paris?": ["2.16 million", []],
    "What is the deepest point in the Pacific Ocean?": ["Mariana Trench", []],
    "How many Harry Potter books are there?": ["7", []],
    "What is the temperature range on Mercury?": ["-290°F to 800°F", []]
}

# Function to display the available questions
def show_questions():
    print("Available Questions:")
    for question in qa_data.keys():
        print("- " + question)

def get_questions():
    return qa_data.keys()

# Function to get the user's answer and provide feedback
def get_answer(question):
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