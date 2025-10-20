# calculator.py

This is a Command Line Interface (CLI) Calculator written in Python.
You can run it directly in a terminal, and it lets you add, subtract, multiply, or divide numbers just by typing choices.

It also has proper error handling, so if you type something wrong (like letters instead of numbers or divide by zero), it doesn’t crash — it just tells you nicely what went wrong.
At the top, we created four small functions — ADD,SUBTRACT,MUTIPLY AND DIVIDE
it just adds both numbers and returns the answer.
Same goes for subtraction, multiplication, and division.

But in division, we added a small check for zero (if n2 == 0:
    return "❌ ERROR: Division by zero!")
    This prevents Python’s “ZeroDivisionError” and instead shows a message(❌ ERROR: Division by zero!).

At the bottom, we just call: 'calculator_cli()' This makes the program start automatically when you run the Python file So as soon as you run the script, it welcomes you and shows the calculator menu.
ERROR handling is intigrated for errors caused bu humans which we often ignore and cheak for code correction
