'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
You're building a number guessing game.

1. Use random.randint to generate a number from 1 to 50.
2. Ask the user to guess the number.
3. If their guess is too low or too high, tell them.
4. Repeat until they get it right.
5. When they guess it, tell them how many tries it took.
'''

# Here is one potential solution. Remember there are often many different
# ways to solve a problem, so your solution may not look exactly the same.

import random

secret = random.randint(1, 50)
guess = -1 # make guess something not equal to secret so the while loop can start.
tries = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 50: "))
    tries += 1
    if guess < secret:
        print("Too low.")
    elif guess > secret:
        print("Too high.")

print(f"You got it in {tries} tries! The number was {secret}.")
