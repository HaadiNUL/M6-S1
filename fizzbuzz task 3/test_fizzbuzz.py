from fizzbuzz import fizzbuzz
def test_fizz():
    assert fizzbuzz(3) == "Fizz", "should return 'Fizz' for multiples of 3"
def test_buzz():
    assert fizzbuzz(5) == "Buzz", "should return 'Buzz' for multiples of 5"
def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz", "should return 'FizzBuzz' for multiples of both 3 and 5" 
def test_number():
    assert fizzbuzz(4) == "4", "should return the number itself if not a multiple of 3 or 5"

        