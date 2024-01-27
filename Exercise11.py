# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.


# pseudocode


# Initialize an empty list to store reversed digits
# Iterate through each digit in reverse order
# Extract the last digit
# Convert digit to string and add to the list
# Remove the last digit from the number
# Join the reversed digits and print the result
# Sample number
# Result


# ********************************* actual code ****************************************************
def extract_digits_reverse_loop(number):
    # Initialize an empty list to store reversed digits
    reversed_digits = []
    
    # Iterate through each digit in reverse order
    while number > 0:
        digit = number % 10 # Extract the last digit
        reversed_digits.append(str(digit))  # Convert digit to string and add to the list
        number //= 10  # Remove the last digit from the number
        
    # Join the reversed digits and print the result
    result = ' '.join(reversed(reversed_digits))
    print(result)
    
# Example usage:
number_example_1 = 7536
extract_digits_reverse_loop(number_example_1)

number_example_2 = 12345
extract_digits_reverse_loop(number_example_2)

    