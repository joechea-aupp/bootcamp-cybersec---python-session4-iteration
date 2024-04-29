# User input with break and continue
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    
    if name.lower() == 'exit':
        print("Exiting the program.")
        break  # Exit the loop if user enters 'exit'
    
    age_str = input("Enter your age: ")
    
    if not age_str.isdigit():
        print("Invalid input. Please enter a valid age.")
        continue  # Skip to the next iteration if age input is not a digit
    
    age = int(age_str)
    
    if age < 0 or age > 120:
        print("Invalid age. Please enter an age between 0 and 120.")
        continue  # Skip to the next iteration if age is invalid
    
    print("Hello, ", name, "! You are", age, "years old.")


