# measure_utils.py

import os
import time
from naive_suffix_array import suffix_array

def read_string_from_file(path):
    """Read and return a string from a text file."""
    with open(path, "r") as f:
        return f.read().strip()

def measure_suffix_array_time(file_path):
    """Measure how long it takes to build a suffix array for a given file."""
    s = read_string_from_file(file_path)
    start = time.perf_counter()
    _ = suffix_array(s)
    end = time.perf_counter()
    elapsed = end - start
    return os.path.basename(file_path), len(s), elapsed

def get_all_txt_files(folder):
    """Get sorted list of all .txt files in a folder."""
    files = [
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".txt")
    ]
    # sort numerically by the length number in filename if present
    files.sort(key=lambda x: int(''.join(filter(str.isdigit, os.path.basename(x)))))
    return files
