#Aim:Write a program in Python that generates a quiz and uses two files – Question.txt and
#Answers.txt. The program open Question.txt and read a question and displays the
#question with option on the screen. The program then opens the Answers.txt file.
# Branch:Comps
# Year:SE
# Sem:IV
# Subject:Python
# Name: Ansari Bushra
# UIN:231P046
# Roll No.:03

def load_questions(filename):
    """Load questions and options from a file."""
    with open(filename, 'r') as file:
        questions = []
        options = []
        
        question = ''
        option_set = []
        
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            # If the line starts with "What", it's a question
            if line[0] == 'W' or line[0] == 'w':
                if question:
                    questions.append((question, option_set))
                question = line
                option_set = []
            else:
                option_set.append(line)
        
        # Add last question
        if question:
            questions.append((question, option_set))
    
    return questions


def load_answers(filename):
    """Load answers from a file."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def display_quiz(questions, answers):
    """Display the quiz and evaluate answers."""
    score = 0
    for i, (question, options) in enumerate(questions):
        print(f"\n{question}")
        for option in options:
            print(option)
        
        user_answer = input("\nYour answer (a, b, c, d): ").lower()
        
        # Check answer
        if user_answer == answers[i]:
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")
    
    print(f"\nYou scored {score}/{len(questions)}")
    print("\nThank You \nName: Ansari Bushra \nUIN:231P046 \nRoll no:03 \n")



def main():
    """Main function to run the quiz program."""
    question_file = 'Question.txt'
    answer_file = 'Answers.txt'
    
    # Load the questions and answers
    questions = load_questions(question_file)
    answers = load_answers(answer_file)
    
    # Ensure there are no mismatched questions and answers
    if len(questions) != len(answers):
        print("Error: The number of questions and answers do not match.")
        return
    
    # Display the quiz
    display_quiz(questions, answers)


if __name__ == "__main__":
    main()
