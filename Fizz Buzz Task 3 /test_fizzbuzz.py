# Import the fizz_buzz function from your fizzbuzz.py module
from fizzbuzz import fizz_buzz

def test_fizz():
    assert fizz_buzz(3) == "Fizz", "Should return 'Fizz' for multiples of 3"

def test_buzz():
    assert fizz_buzz(5) == "Buzz", "Should return 'Buzz' for multiples of 5"

def test_fizzbuzz():
    assert fizz_buzz(15) == "FizzBuzz", "Should return 'FizzBuzz' for multiples of both 3 and 5"

def test_number():
    assert fizz_buzz(2) == "2", "Should return the number itself if not a multiple of 3 or 5"

def test_negative():
    assert fizz_buzz(-3) == "Fizz", "Should handle negative numbers correctly for multiples of 3"

def test_zero():
    assert fizz_buzz(0) == "FizzBuzz", "Zero should be considered a multiple of any number"
