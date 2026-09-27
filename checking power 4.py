"""
1) Add the file and topic details.
   a) Mention the file name as `03-power-of-4.py`.
   b) Mention the topic as "Checking Powers of 4 with Recursion, Two Stopping Conditions".
   c) Introduce the program as a way to check powers of 4 recursively.

2) Create the recursive function.
   a) Define a function named `is_power4(n)`.
   b) Use `n` as the number that is checked and divided.

3) Add the first stopping condition.
   a) Check if `n <= 0`.
   b) Return `False` because powers of 4 must be positive.

4) Add the true stopping condition.
   a) Check if `n == 1`.
   b) Return `True` because dividing a power of 4 eventually reaches 1.

5) Add the recursive case.
   a) Check if `n % 4 == 0`.
   b) Divide the number by 4 using `n // 4`.
   c) Call `is_power4()` again with the smaller number.

6) Add the false case.
   a) Return `False` when the number is not divisible by 4.
   b) Use this to stop numbers that are not powers of 4.

7) Show fixed examples.
   a) Pause before showing the examples.
   b) Print `is_power4(16)`.
   c) Print `is_power4(12)`.

8) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 64 or 48.
   c) Convert the input into an integer.

9) Ask for a prediction.
   a) Ask the user to guess whether the number is a power of 4.
   b) Store the user's guess.

10) Display the final result.
   a) Pause before showing the answer.
   b) Call `is_power4(n)` using the user's number.
   c) Print the result and the user's original guess.
"""
# Checking Powers of 4 with Recursion, Two Stopping Conditions
def is_power4(n):
   if n <=0:
      return False
   if n == 1:
      return True
   if n % 4 == 0:
      return is_power4(n // 4)
   return False
input("is_power4: check if the number is a power of 4 with two stopping conditions press enter")
print("is_power4(16) =", is_power4(16))
print("is_power4(12) =", is_power4(12))
n = int(input("Enter a number to check if it's a power of 4 (eg, 46,64): "))
guess = input("What do you think? Is it a power of 4? (Enter True or False): ")
input("is_power4(n) press enter")
print("is_power4(" + str(n) + ") =", is_power4(n), "your guess was", guess)