# Write a short recursive Python function that rearranges a sequence of integer
# values so that all the even values appear before all the odd values.

def even_odd(lst, sorted=[], i=0, j=0):
    if i < len(lst):
        if lst[i] % 2 == 0:
            sorted.append(lst[i])
            return even_odd(lst, sorted, i+1, j)
        else:
            return even_odd(lst, sorted, i+1, j)

    elif j < len(lst):
        if lst[j] % 2 == 1:
            sorted.append(lst[j])
            return even_odd(lst, sorted, i, j+1)
        else:
            return even_odd(lst, sorted, i, j+1)

    else:
        return sorted


Nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,24]

arranged_list = even_odd(Nums)
print(arranged_list)

