
"""Mandatory Project Part 1/3"""

"""This project implements the naive algorithm for constructing suffix trees and measures its performance across different input strings.

To run the sequential performance measurement: python sequential_measure.py --num_files 5

--num_files specifies how many files to process from each folder (default: 10).

To get the banana suffix array, run the naive_suffix_array.py script.

The script will:

Measure the time required to build suffix arrays for each input file.
Save results in suffix_array_partial_results.csv.
Generate and display a plot (suffix_array_times_sequential.png) comparing running times.

Files

sequential_measure.py → main script to run experiments
measure_utils.py → helper functions for file handling and timing
naive_suffix_array.py → naive implementation of the suffix array algorithm

Output

A CSV file with partial timing results.
A plot showing time vs. input size for both “all a’s” and random strings.
"""

def suffix_array(s):
    """Build a suffix array in O(n log n) using Python's sorting."""
    return sorted(range(len(s)), key=lambda k: s[k:])

x = "banana"
SA = suffix_array(x)
print("Suffix array:", SA)


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

# Results of testing in Figure suffix_array_times_sequential1.png, obtained after running the sequential_measure.py script on the provided folders with different string types and lengths.

# Our results show that the all_a_strings run equally fast as the random strings for strings as long as 90.000, after that we see an increase of time for the randoms strings, 
# for lengths 100.000 and 200.000 which is opposite of what we expected. We expected the all_a_strings to be slower than the random strings, because of the long common prefix 
# that makes the comparisons take longer time. We could not measure for longer strings because of memory issues. However, we would expect that for longer strings we would find 
# that the all_a_strings would be slower than the random strings.