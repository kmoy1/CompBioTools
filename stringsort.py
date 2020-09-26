def merge(left, right):
    result = []
    i, j = 0, 0
    while(i < len(left) and j< len(right)):
        if(left[i][0] <= right[j][0]): #Compare strings.
            # print(i)
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1

    result += left[i:]
    result += right[j:]
    return result

def mergesort(pairs):
    """Given set PAIRS representing (suffix, suffix ID) of some string S, use mergesort to lexicographically sort.
    Runtime: O(n^2*logn), where n = |S|. Sorting takes O(n*logn) comparisons, each comparison taking O(n). 
    Return sorted pairs.
    """
    if len(pairs) < 2:
        return pairs
    M = len(pairs) // 2
    L = mergesort(pairs[:M])
    R = mergesort(pairs[M:])
    return merge(L, R)
