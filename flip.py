"""
1) Add the file and topic details.
   a) Mention the file name as `01-digit-flip.py`.
   b) Mention the topic as "Digit Extraction with % and //, Reversing a Number with Recursion".
   c) Introduce the program as a way to reverse a number using recursion.

2) Create the recursive function.
   a) Define a function named `flip_number(num)`.
   b) Use `num` as the number that becomes smaller in every recursive call.

3) Add the base case.
   a) Check if `num // 10 == 0`.
   b) Return `num` when only one digit is left.
   c) Use this base case to stop recursion.

4) Extract and reverse digits.
   a) Use `num % 10` to get the last digit.
   b) Use `num // 10` to remove the last digit.
   c) Recursively flip the remaining digits.
   d) Place the last digit at the front using powers of 10.

5) Show fixed examples.
   a) Pause before showing the examples.
   b) Print `flip_number(123)`.
   c) Print `flip_number(456)`.

6) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 789 or 1234.
   c) Convert the input into an integer.

7) Ask for a prediction.
   a) Ask the user to guess the reversed number.
   b) Store the user's guess.

8) Display the final result.
   a) Pause before showing the answer.
   b) Call `flip_number(n)` using the user's number.
   c) Print the reversed number and the user's original guess.
"""
# Digt Extraction with %  and //  Rversing a number wuth recursion
def flip_number(num):
   if num // 10 == 0:
      return num 
   else:
      LastDigit = num % 10
      remaining = num // 10
      return LastDigit * pow(10, len(str(remaining))) + flip_number(remaining)
input("flip number: extract the last digit with % and remove it with // press enter")
print("flip_number(123) =", flip_number(123))
print("flip_number(456) =", flip_number(456))
n = int(input("Enter a number to reverse (eg. 546,235):"))
guess = input("What do you think the reversed number will be? (Enter a number): ")
input("flip_number(n) press enter")
print("flip_number(" + str(n) + ") =", flip_number(n), "your guess was", guess)