#this is a test main file
import os
import sys

def main():
    print("This is the main function of the script.")
    print("Current working directory:", os.getcwd())
    print("Python version:", sys.version)

    # Example functionality: simple arithmetic operation
    result = 2 + 2
    print("Result of 2 + 2 is:", result)
    result = 2 * 3
    print("Result of 2 * 3 is:", result)
    greet("User")

def greet(name):
    """Function to greet a user."""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()