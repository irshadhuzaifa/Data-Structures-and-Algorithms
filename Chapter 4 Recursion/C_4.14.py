# Define a function to solve the Towers of Hanoi puzzle

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
c = []

def Hanoi(n, i=-1, j=-1):
    # If i is within the bounds of the list 'n' (checking from the end of the list)
    if i >= -len(n):
        # Append the element from 'a' at index 'i' to list 'b'
        b.append(a[i])
        # Recur with i decremented by 1 to continue appending elements from 'a' to 'b'
        return Hanoi(n, i-1)
    # If i has gone out of bounds but j is still within the bounds of the list 'n'
    elif j >= -len(n):
        # Append the element from 'b' at index 'j' to list 'c'
        c.append(b[j])
        # Recur with j decremented by 1 to continue appending elements from 'b' to 'c'
        return Hanoi(n, i, j-1)
    else:
        # If both i and j have gone out of bounds, return the three lists
        return a, b, c

# Call the Hanoi function and print the results
print(Hanoi(a))

