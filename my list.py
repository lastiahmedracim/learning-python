"""
Collection of Python Programs
Contains various utility functions and games
"""

import random
import time
import string
import math
from collections import Counter

# ============ 1. Custom max() function ============
def my_max(*args):
    """Find maximum value from given arguments"""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]
    
    if not args:
        return None
    
    max_val = args[0]
    for num in args[1:]:
        if num > max_val:
            max_val = num
    return max_val

# ============ 2. Custom min() function ============
def my_min(*args):
    """Find minimum value from given arguments"""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        args = args[0]
    
    if not args:
        return None
    
    min_val = args[0]
    for num in args[1:]:
        if num < min_val:
            min_val = num
    return min_val

# ============ 3. Recursive Factorial ============
def factorial(n):
    """Calculate factorial recursively"""
    if n < 0:
        return None
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# ============ 4. Recursive Fibonacci ============
def fibonacci(n):
    """Calculate nth Fibonacci number recursively"""
    if n < 0:
        return None
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# ============ 5. Armstrong Number Check ============
def is_armstrong(num):
    """Check if number is an Armstrong number"""
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == num

# ============ 6. Count Word Frequency ============
def word_frequency(text):
    """Count frequency of each word in text"""
    words = text.lower().split()
    return dict(Counter(words))

# ============ 7. GCD and LCM ============
def gcd(a, b):
    """Find Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Find Least Common Multiple"""
    return abs(a * b) // gcd(a, b)

# ============ 8. Decimal to Binary ============
def decimal_to_binary(n):
    """Convert decimal to binary"""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

# ============ 9. Binary to Decimal ============
def binary_to_decimal(binary_str):
    """Convert binary string to decimal"""
    decimal = 0
    for i, digit in enumerate(reversed(binary_str)):
        decimal += int(digit) * (2 ** i)
    return decimal

# ============ 10. Caesar Cipher ============
def caesar_cipher(text, shift, decrypt=False):
    """Encrypt or decrypt text using Caesar cipher"""
    if decrypt:
        shift = -shift
    
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# ============ 11. Pig Latin Translator ============
def pig_latin(text):
    """Translate text to Pig Latin"""
    words = text.split()
    result = []
    
    for word in words:
        if word[0].lower() in 'aeiou':
            result.append(word + 'way')
        else:
            # Find first vowel
            for i, char in enumerate(word):
                if char.lower() in 'aeiou':
                    result.append(word[i:] + word[:i] + 'ay')
                    break
            else:
                result.append(word + 'ay')
    
    return ' '.join(result)

# ============ 12. Generate Random Password ============
def generate_password(length=12, use_upper=True, use_lower=True, 
                      use_digits=True, use_special=True):
    """Generate a random password"""
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    if not chars:
        return "Error: No character types selected"
    
    return ''.join(random.choice(chars) for _ in range(length))

# ============ 13. Dice Simulator ============
def roll_dice(sides=6):
    """Simulate rolling a dice"""
    return random.randint(1, sides)

# ============ 14. Lottery Number Generator ============
def generate_lottery_numbers(count=6, min_num=1, max_num=49):
    """Generate unique lottery numbers"""
    if count > (max_num - min_num + 1):
        return "Error: Too many numbers requested"
    
    return sorted(random.sample(range(min_num, max_num + 1), count))

# ============ 15. Stopwatch ============
def stopwatch():
    """Simple stopwatch function"""
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    elapsed = end_time - start_time
    return f"Elapsed time: {elapsed:.2f} seconds"

# ============ 16. Countdown Timer ============
def countdown_timer(seconds):
    """Display a countdown timer"""
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# ============ 17. Prime Number Generator ============
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate prime numbers up to a limit"""
    return [i for i in range(2, limit + 1) if is_prime(i)]

# ============ 18. Perfect Number Checker ============
def is_perfect_number(n):
    """Check if a number is perfect"""
    if n < 1:
        return False
    
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# ============ 19. Multiplication Quiz ============
def multiplication_quiz(num_questions=5, max_num=12):
    """Multiplication quiz game"""
    correct = 0
    
    for i in range(num_questions):
        a = random.randint(1, max_num)
        b = random.randint(1, max_num)
        
        try:
            answer = int(input(f"Question {i+1}: {a} × {b} = "))
            if answer == a * b:
                print("Correct! ✓")
                correct += 1
            else:
                print(f"Wrong! The answer is {a * b}")
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\nScore: {correct}/{num_questions} ({correct/num_questions*100:.1f}%)")
    return correct

# ============ 20. Math Quiz Game ============
def math_quiz(num_questions=5, max_num=20):
    """General math quiz with addition, subtraction, multiplication"""
    operations = ['+', '-', '*']
    correct = 0
    
    for i in range(num_questions):
        a = random.randint(1, max_num)
        b = random.randint(1, max_num)
        op = random.choice(operations)
        
        # Ensure subtraction doesn't go negative
        if op == '-' and a < b:
            a, b = b, a
        
        question = f"Question {i+1}: {a} {op} {b} = "
        
        try:
            answer = int(input(question))
            if op == '+':
                correct_answer = a + b
            elif op == '-':
                correct_answer = a - b
            else:
                correct_answer = a * b
            
            if answer == correct_answer:
                print("Correct! ✓")
                correct += 1
            else:
                print(f"Wrong! The answer is {correct_answer}")
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\nScore: {correct}/{num_questions} ({correct/num_questions*100:.1f}%)")
    return correct

# ============ Demo Functions ============
def demo_programs():
    """Demonstrate all functions"""
    
    print("=" * 50)
    print("DEMONSTRATION OF ALL PROGRAMS")
    print("=" * 50)
    
    # 1 & 2. max and min
    print("\n1 & 2. Custom max() and min():")
    numbers = [3, 7, 1, 9, 4]
    print(f"Numbers: {numbers}")
    print(f"Max: {my_max(numbers)}")
    print(f"Min: {my_min(numbers)}")
    
    # 3. Factorial
    print(f"\n3. Factorial of 5: {factorial(5)}")
    
    # 4. Fibonacci
    print(f"4. Fibonacci of 10: {fibonacci(10)}")
    
    # 5. Armstrong
    print(f"5. Is 153 Armstrong? {is_armstrong(153)}")
    print(f"   Is 154 Armstrong? {is_armstrong(154)}")
    
    # 6. Word frequency
    text = "the cat and the dog and the mouse"
    print(f"6. Word frequency of '{text}':")
    print(f"   {word_frequency(text)}")
    
    # 7. GCD and LCM
    print(f"7. GCD(12, 18) = {gcd(12, 18)}")
    print(f"   LCM(12, 18) = {lcm(12, 18)}")
    
    # 8 & 9. Binary conversion
    print(f"8. Decimal 42 to binary: {decimal_to_binary(42)}")
    print(f"9. Binary 101010 to decimal: {binary_to_decimal('101010')}")
    
    # 10. Caesar cipher
    text = "Hello World!"
    encrypted = caesar_cipher(text, 3)
    decrypted = caesar_cipher(encrypted, 3, decrypt=True)
    print(f"10. Caesar cipher:")
    print(f"    Original: {text}")
    print(f"    Encrypted: {encrypted}")
    print(f"    Decrypted: {decrypted}")
    
    # 11. Pig Latin
    print(f"11. Pig Latin: 'hello world' -> {pig_latin('hello world')}")
    
    # 12. Password
    print(f"12. Random password: {generate_password(12)}")
    
    # 13. Dice
    print(f"13. Dice roll: {roll_dice()}")
    
    # 14. Lottery
    print(f"14. Lottery numbers: {generate_lottery_numbers()}")
    
    # 15 & 16. Stopwatch and countdown (commented to avoid waiting)
    # print("\n15. Stopwatch will run on demand")
    # print("16. Countdown timer will run on demand")
    
    # 17. Prime numbers
    print(f"17. Prime numbers up to 20: {generate_primes(20)}")
    
    # 18. Perfect number
    print(f"18. Is 28 perfect? {is_perfect_number(28)}")
    print(f"    Is 10 perfect? {is_perfect_number(10)}")
    
    # 19 & 20. Quizzes (simplified demo)
    print("\n19 & 20. Quiz games available (run multiplication_quiz() or math_quiz())")

# ============ Interactive Menu ============
def main():
    """Main interactive menu"""
    print("\n" + "=" * 50)
    print(" PYTHON UTILITY PROGRAMS MENU ")
    print("=" * 50)
    print("1.  Custom max() function")
    print("2.  Custom min() function")
    print("3.  Recursive factorial")
    print("4.  Recursive Fibonacci")
    print("5.  Check Armstrong numbers")
    print("6.  Count word frequency")
    print("7.  Find GCD and LCM")
    print("8.  Decimal to binary converter")
    print("9.  Binary to decimal converter")
    print("10. Caesar cipher")
    print("11. Pig Latin translator")
    print("12. Generate random passwords")
    print("13. Dice simulator")
    print("14. Lottery number generator")
    print("15. Stopwatch")
    print("16. Countdown timer")
    print("17. Prime number generator")
    print("18. Perfect number checker")
    print("19. Multiplication quiz")
    print("20. Math quiz game")
    print("0.  Run all demos")
    print("q.  Quit")
    print("=" * 50)
    
    while True:
        choice = input("\nEnter your choice: ").strip().lower()
        
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == '0':
            demo_programs()
        elif choice == '1':
            nums = input("Enter numbers separated by spaces: ").split()
            nums = [float(n) for n in nums]
            print(f"Max: {my_max(nums)}")
        elif choice == '2':
            nums = input("Enter numbers separated by spaces: ").split()
            nums = [float(n) for n in nums]
            print(f"Min: {my_min(nums)}")
        elif choice == '3':
            n = int(input("Enter a number: "))
            print(f"Factorial of {n}: {factorial(n)}")
        elif choice == '4':
            n = int(input("Enter a number: "))
            print(f"Fibonacci of {n}: {fibonacci(n)}")
        elif choice == '5':
            n = int(input("Enter a number: "))
            print(f"{n} is {'an Armstrong' if is_armstrong(n) else 'not an Armstrong'} number")
        elif choice == '6':
            text = input("Enter text: ")
            print(f"Word frequency: {word_frequency(text)}")
        elif choice == '7':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"GCD: {gcd(a, b)}")
            print(f"LCM: {lcm(a, b)}")
        elif choice == '8':
            n = int(input("Enter decimal number: "))
            print(f"Binary: {decimal_to_binary(n)}")
        elif choice == '9':
            s = input("Enter binary string: ")
            print(f"Decimal: {binary_to_decimal(s)}")
        elif choice == '10':
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            print(f"Encrypted: {caesar_cipher(text, shift)}")
            print(f"Decrypted: {caesar_cipher(text, shift, decrypt=True)}")
        elif choice == '11':
            text = input("Enter text: ")
            print(f"Pig Latin: {pig_latin(text)}")
        elif choice == '12':
            length = int(input("Enter password length (default 12): ") or 12)
            print(f"Password: {generate_password(length)}")
        elif choice == '13':
            sides = int(input("Enter number of sides (default 6): ") or 6)
            print(f"Rolled: {roll_dice(sides)}")
        elif choice == '14':
            count = int(input("How many numbers? (default 6): ") or 6)
            print(f"Lottery numbers: {generate_lottery_numbers(count)}")
        elif choice == '15':
            print(stopwatch())
        elif choice == '16':
            seconds = int(input("Enter seconds for countdown: "))
            countdown_timer(seconds)
        elif choice == '17':
            limit = int(input("Enter limit: "))
            print(f"Prime numbers up to {limit}: {generate_primes(limit)}")
        elif choice == '18':
            n = int(input("Enter a number: "))
            print(f"{n} is {'a perfect' if is_perfect_number(n) else 'not a perfect'} number")
        elif choice == '19':
            q = int(input("How many questions? (default 5): ") or 5)
            multiplication_quiz(q)
        elif choice == '20':
            q = int(input("How many questions? (default 5): ") or 5)
            math_quiz(q)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
