# Write a short recursive Python function that finds the minimum and maximum
# values in a sequence without using any loops.

Nums = [1,2,3,4,10,45,82,9,10,8,7,6,5]

def max_min(lst, i=0, max=None, min=None):
    if i < len(lst):
        if min==None or lst[i] < min:
            min = lst[i]
        if  max==None or lst[i] > max:
            max = lst[i]
        return max_min(lst, i+1, max, min)

    else:
        return max, min

maximum, minimum = max_min(Nums)

print("Maximum:", maximum)
print("Minimum:", minimum)

