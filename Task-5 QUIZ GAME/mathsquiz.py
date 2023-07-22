import random

# Quiz Questions
quiz_questions = [
    {
        "question": "What is the value of 3² + 4³?",
        "choices": ["A. 29", "B. 47", "C. 63", "D. 73"],
        "answer": "D. 73"
    },
    {
        "question": "Calculate the area of a rectangle with length 6 units and width 8 units.",
        "choices": ["A. 20 square units", "B. 24 square units", "C. 30 square units", "D. 48 square units"],
        "answer": "D. 48 square units"
    },
    {
        "question": "Find the value of 'x': 3x - 2 = 10",
        "choices": ["A. x = 3", "B. x = 4", "C. x = 5", "D. x = 6"],
        "answer": "B. x = 4"
    },
    {
        "question": "What is the square root of 169?",
        "choices": ["A. 10", "B. 12", "C. 13", "D. 15"],
        "answer": "C. 13"
    },
    {
        "question": "Solve for x: 2x + 1 = 15",
        "choices": ["A. x = 5", "B. x = 7", "C. x = 8", "D. x = 10"],
        "answer": "B. x = 7"
    }
]

# Function to load a random question
def get_random_question():
    return random.choice(quiz_questions)

# Function to present the quiz questions
def present_quiz_questions():
    score = 0
    remaining_questions = quiz_questions.copy()
    random.shuffle(remaining_questions)

    for i, question in enumerate(remaining_questions):
        print(f"\nQuestion {i+1}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        user_answer = input("Enter your answer (e.g., A, B, C, D): ")
        if user_answer.lower() == question['answer'][0].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print(f"The correct answer is: {question['answer']}")
    
    return score

# Display welcome message and rules
print("Welcome to the Quiz Game!")
print("You will be presented with multiple-choice questions.")
print("Choose the correct answer by typing the corresponding letter.")
print("Let's get started!")

play_again = True
while play_again:
    # Present quiz questions
    score = present_quiz_questions()

    # Calculate final score
    total_questions = len(quiz_questions)
    percentage = (score / total_questions) * 100

    # Display final results
    print("\n--- Quiz Results ---")
    print(f"You scored {score} out of {total_questions} questions. ({percentage}%)")
    if percentage == 100:
        print("Congratulations! You got a perfect score!")
    elif percentage >= 75:
        print("Well done! You did a great job!")
    elif percentage >= 50:
        print("Not bad! Keep improving!")
    else:
        print("Better luck next time!")

    # Ask the user if they want to play again
    play_again_input = input("Do you want to play again? (yes/no): ")
    play_again = play_again_input.lower() == "yes"
