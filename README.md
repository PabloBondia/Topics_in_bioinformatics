# Topics_in_bioinformatics

This project implements the naive algorithm for constructing suffix trees and measures its performance across different input strings.

To run the sequential performance measurement: python sequential_measure.py --num_files 5

--num_files specifies how many files to process from each folder (default: 10).


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
