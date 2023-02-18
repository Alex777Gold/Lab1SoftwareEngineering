# Importing necessary libraries
import random

# Defining a list of responses
responses = ["I'm doing well, thank you!", "Not too bad, how about you?", "I'm great!"]

# Defining the main function
def main():
    print("Hello, how are you?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        else:
            response = random.choice(responses)
            print(response)

# Calling the main function
if __name__ == "__main__":
    main()
