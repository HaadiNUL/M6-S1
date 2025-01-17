import random

def make_arithmetic_problem():
    # This function generates an arithmetic equation where we solve for 'x'.
    # It randomly chooses numbers and an operator, then formats the equation.
    # Example output: "5 + x = 10", with 'x' being 5.
    
    operators = ['+', '-', '*']  # Keeping it simple for now
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    chosen_op = random.choice(operators)  # Pick an operator randomly
    
    # Determine the result based on the chosen operation
    if chosen_op == '+':
        result = num1 + num2
    elif chosen_op == '-':
        result = num1 - num2
    elif chosen_op == '*':
        result = num1 * num2
    else:
        # This shouldn't happen, but better safe than sorry
        raise ValueError("Unexpected operator!")
    
    # Creating the formatted equation string
    equation = f"{num1} {chosen_op} x = {result}"
    return equation, num2  # Return the problem and the correct answer for 'x'

def run_math_quiz():
    """
    Main logic for running the math quiz.
    The user will be prompted with math problems, and their answers will be checked.
    """
    print("Welcome to the Math Quiz!")
    print("Your goal: Solve for 'x' in each equation.")

    total_score = 0
    total_questions = 5  # Let's keep the quiz short and sweet
    
    for question_num in range(1, total_questions + 1):
        print(f"\nQuestion {question_num}:")
        
        # Generate a math problem
        equation, correct_x = make_arithmetic_problem()
        print(equation)
        
        try:
            user_input = input("Enter your answer for x: ").strip()
            user_answer = int(user_input)  # Convert to integer
            
            # Check if the answer is correct
            if user_answer == correct_x:
                print("Correct! Nicely done!")
                total_score += 1
            else:
                print(f"Oops, not quite. The correct answer was {correct_x}.")
        except ValueError:
            # Handle cases where input isn't a valid integer
            print("Hmm, that doesn't look like a number. Remember to type an integer!")
    
    # Wrap up the quiz
    print(f"\nThat's the end of the quiz! You scored {total_score} out of {total_questions}.")
    print("Thanks for playing. Come back to try again!")

# Only run the quiz if this script is executed directly
if __name__ == '__main__':
    run_math_quiz()