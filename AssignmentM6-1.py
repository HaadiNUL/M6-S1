import random

def generate_equation():
    """
    Generates a simple arithmetic equation with one unknown 'x'.
    This function randomly selects numbers and an operator, computes the result,
    and formats it as an equation of the form 'a op x = result'.
    
    Returns:
        tuple: A tuple containing the formatted equation (str) and the correct value of 'x' (int).
    """
    operators = ['+', '-', '*']
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(operators)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b

    equation = f"{a} {op} x = {result}"
    return equation, b

def main():
    """
    Main function to conduct a math quiz. Generates equations, takes user input,
    and checks answers, tracking the total score.
    """
    score = 0
    num_questions = 5

    print("Welcome to the Math Quiz! Please solve for x in each equation.")

    for i in range(1, num_questions + 1):
        print(f"\nQuestion {i}:")
        equation, correct_answer = generate_equation()
        print(equation)
        
        try:
            user_answer = int(input("Your answer for x: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {correct_answer}")
        except ValueError:
            print("Invalid input; please enter a valid integer.")

    print(f"\nGame over! Your total score is: {score} out of {num_questions}")

if __name__ == "__main__":
    main()