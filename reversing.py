"""
1) Add the file and topic details.
   a) Mention the file name as `02-flip-name.py`.
   b) Mention the topic as "Reversing a String with Recursion".
   c) Introduce the program as a way to reverse text using recursion.

2) Create the recursive function.
   a) Define a function named `flip_name(s)`.
   b) Use `s` as the string that becomes smaller in every recursive call.

3) Add the base case.
   a) Check if the string length is 1.
   b) Return the single character when only one character is left.
   c) Use this base case to stop recursion.

4) Add the recursive case.
   a) Use `s[1:]` to take the string without the first character.
   b) Recursively flip the remaining string.
   c) Add `s[0]` at the end.
   d) Show how the first character lands last.

5) Show fixed examples.
   a) Pause before showing the examples.
   b) Print `flip_name('Maya')`.
   c) Print `flip_name('Code')`.

6) Ask for a name.
   a) Ask the user to enter a name.
   b) Suggest example names like Riya or Dev.
   c) Store the input in `name`.

7) Ask for a prediction.
   a) Ask the user to guess the flipped name.
   b) Store the user's guess.

8) Display the final result.
   a) Pause before showing the answer.
   b) Call `flip_name(name)` using the user's input.
   c) Print the flipped name and the user's original guess.
"""
# Reversing a String with Recursion
def flip_name(s):
    if len(s)==1:
        return s
    else:
        return flip_name(s[1:]) + s[0]
input("flip name: take the string without the first character and add the first character at the end press enter")
print("flip_name('Maya') =", flip_name('Maya'))
print("flip_name('Code') =", flip_name('Code'))
name = input("Enter a name to flip (eg. Riya, Dev): ")
guess = input("What do you think the flipped name will be? (Enter a string): ")
input("flip_name(name) press enter")
print("flip_name(" + name + ") =", flip_name(name), "your guess was", guess)