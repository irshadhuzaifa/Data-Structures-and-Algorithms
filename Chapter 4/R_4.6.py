# Define a recursive function to compute the nth Harmonic number
# The Harmonic number Hn is defined as the sum of the reciprocals of the first n natural numbers
# Hn = Σ (1/i) for i from 1 to n

def harmonic_num(n, i=1):
    # Base case: if i is greater than n, return 0
    if i <= n:
        # Recursive case: add the reciprocal of i to the result of the next call
        return 1/i + harmonic_num(n, i+1)
    else:
        # End of recursion: return 0 when i is greater than n
        return 0

# Compute the 5th Harmonic number
fifth_harmonic = harmonic_num(5)

# Print the result
print(fifth_harmonic)  # Output: 2.283333333333333