# Use recursion to write a Python function for determining if a string s has
# more vowels than consonants.

def vow_cons (str, i=0, vow=['a','e','i','o','u'], v=0, c=0):
    if i < len(str):
        if str[i] not in vow:
            c += 1
            return vow_cons(str, i+1, vow, v, c)
        else:
            v += 1
            return vow_cons(str, i+1, vow, v, c)

    else:
        return v, c

vowels, conosonants = vow_cons("abcdefghijklmnopqrstuvwxyz")
print("Vowels: ", vowels)
print("Consonants: ", conosonants)
