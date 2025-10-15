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

x = "banana"
SA = suffix_array(x)
print("Suffix array:", SA)

print(search_pattern(x, SA, "ssi"))   # -> 0
print(search_pattern(x, SA, "ippi"))   # -> 1
print(search_pattern(x, SA, "x"))   # -> -1





### Questions: ###

# 0. You must explain how to use your code to construct a suffix array, and show its output (the suffix array) for the input banana. 

# To run the code and generate the suffix array for the input "banana", simply execute the script. The function `suffix_array` constructs 
# the suffix array, and the output is printed to the console.
# The Suffix array for the input "banana" is: [5, 3, 1, 0, 4, 2]

# 1. What is the worst case running time for constructing a suffix array of a string of length n? 

# The worst-case running time for constructing a suffix array of a string of length n using the provided method is O(n^2 log n). 

# 1.1 Explain why? 

# The sorting step involves comparing suffixes, and in the worst case, comparing two suffixes can take O(n) time (when they share a long common prefix).
# Since there are n suffixes to sort, the overall complexity becomes O(n * n log n) = O(n^2 log n).


# 2. Do you think that constructing a suffix array of an identical string is slower than constructing a suffix array of a random string? 

# Constructing a suffix array of an identical string is generally slower than constructing a suffix array of a random string. 

# 2.1 Explain why?

# In an identical string, many suffixes will share long common prefixes, leading to more comparisons during the sorting process. 
# Each comparison can take O(n) time in the worst case, resulting in a higher overall time complexity. 
# In contrast, a random string is less likely to have long common prefixes among its suffixes, leading to fewer comparisons and faster sorting.


# 3 You must comment on how your measurements compare to your expectation of the running time of your method/program on the different types and lengths of strings. 

# Our results show that the all_a_strings run equally fast as the random strings for strings as long as 90.000, after that we see an increase of time for the randoms strings, 
# for lengths 100.000 and 200.000 which is opposite of what we expected. We expected the all_a_strings to be slower than the random strings, because of the long common prefix 
# that makes the comparisons take longer time. We could not measure for longer strings because of memory issues. However, we would expect that for longer strings we would find 
# that the all_a_strings would be slower than the random strings.