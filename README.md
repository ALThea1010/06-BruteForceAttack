This program simulates a password system and gives you a glimpse into how a brute force attack works to crack passwords.

Here’s what it does:

Set Up the Password: It starts by defining a correct password, which in this case is "meow." You also have a limit on how many attempts you can make—five tries to get it right.

Brute Force Function: The program includes a function that generates all possible combinations of printable characters to guess the password. It keeps track of how many attempts it takes until it finds the correct one.

Guessing Using Recursion: There’s another function that tries to guess the password using a more systematic approach, focusing on lowercase letters.

Password Entry: The main part of the program asks you to enter the password. If you get it right, it grants you access. If you enter the wrong password, it lets you know how many attempts you have left. If you hit the maximum number of tries, it warns you that authorities have been alerted.

Running the Program: When you run the program, you get to see how it handles password entry and how it could theoretically guess the password using brute force.
