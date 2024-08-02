# Initial list of numbers
Nums = [1, 2, 3, 4, 5, 6, 10, 20, 8, 9, 7]

# Non-recursive approach to generate all subsets
def subsets(lst):
    i = 0
    j = 0
    subs = []

    while i < len(lst):
        j = i + 1
        while j <= len(lst):
            subs.append(lst[i:j])
            j += 1

        i += 1

    return subs

# Get subsets using non-recursive approach
sub_lists = subsets(Nums)
print(sub_lists)

# Recursive approach to generate all subsets
def recursive_subsets(lst, rec_subs=[], i=0, j=1):
    # If j is within bounds, add the current subset to rec_subs and recurse
    if j <= len(lst):
        rec_subs.append(lst[i:j])
        return recursive_subsets(lst, rec_subs, i, j+1)
    # If j is out of bounds but i is within bounds, increment i and reset j
    elif i < len(lst):
        j = i + 2
        return recursive_subsets(lst, rec_subs, i + 1, j)
    # If both i and j are out of bounds, return the collected subsets
    else:
        return rec_subs

# Get subsets using recursive approach
recursion_subs = recursive_subsets(Nums)
print(recursion_subs)
