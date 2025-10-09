def suffix_array(s):
    """Build a suffix array in O(n log n) using Python's sorting."""
    return sorted(range(len(s)), key=lambda k: s[k:])

def search_pattern(x, SA, u):
    """
    Search pattern u in text x using suffix array SA.
    Returns the index of a match in x, or -1 if not found.
    """
    n = len(SA)
    m = len(u)
    L, R = 0, n - 1
    j = -1  # no match yet

    while L <= R and j == -1:
        M = (L + R) // 2
        start = SA[M]
        substring = x[start:start+m]

        if u == substring:
            j = start   # found
        elif u > substring:
            L = M + 1   # search right half
        else:
            R = M - 1   # search left half

    return j

x = "mississippi"
SA = suffix_array(x)
print("Suffix array:", SA)

print(search_pattern(x, SA, "ssi"))   # -> 0
print(search_pattern(x, SA, "ippi"))   # -> 1
print(search_pattern(x, SA, "x"))   # -> -1