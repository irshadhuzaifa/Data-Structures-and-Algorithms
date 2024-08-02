# Define a recursive function that takes a string of digits as input.

def str_to_digit(str):
    # Base case: if the string is empty, return 0.
    if str == "":
        return 0
    else:
        # Convert the first character of the string to an integer.
        digit = int(str[0])

        # Calculate the position of this digit from the left.
        # This is equivalent to the total length of the string minus 1.
        n = len(str) - 1

        # Calculate the value of the current digit in its correct position by multiplying
        # the digit by 10 raised to the power of n (its position from the left).
        # Then, add the result of the recursive call on the substring excluding the first character.
        return digit * 10 ** n + str_to_digit(str[1:])


# Example usage:
# Convert the string '13554531' to the corresponding integer.
string_digit = str_to_digit('13554531')

# Print the resulting integer.
print(string_digit)
