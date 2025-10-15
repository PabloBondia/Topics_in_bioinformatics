
""" Mandatory Project Part 3/3"""


import matplotlib.pyplot as plt
from measure_utils import measure_suffix_array_time, get_all_txt_files
import csv
import argparse

# run like this: python sequencial_measure.py --num_files 5

def main():
    # --- Argparse setup ---
    parser = argparse.ArgumentParser(description="Measure suffix array construction times.")
    parser.add_argument("--num_files", type=int, default=10, help="Number of files to process from each folder")
    args = parser.parse_args()

    # Folders (keep your defaults)
    all_a_dir = "all_a_str"
    random_dir = "random_str"

    # Take only the first N files from each folder
    all_a_files = get_all_txt_files(all_a_dir)[:args.num_files]
    random_files = get_all_txt_files(random_dir)[:args.num_files]

    print(f"Processing {len(all_a_files)} 'all a' files and {len(random_files)} random files.")

    results_all_a = []
    results_random = []

    # Sequential measurement
    for file_path in all_a_files + random_files:
        try:
            name, length, time_s = measure_suffix_array_time(file_path)

            if "all_a" in name:
                results_all_a.append((length, time_s))
            else:
                results_random.append((length, time_s))

            print(f"{name:<30} | {length:>8} | {time_s:>8.4f}s")

            # Save partial results to CSV
            with open("suffix_array_partial_results.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name, length, time_s])

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    # Sort results for plotting
    results_all_a.sort(key=lambda x: x[0])
    results_random.sort(key=lambda x: x[0])

    if not results_all_a or not results_random:
        print("No results to plot. Check if your folders and files exist.")
        return

    # Unpack for plotting
    lengths_all_a, times_all_a = zip(*results_all_a)
    lengths_random, times_random = zip(*results_random)

    # Plot
    plt.figure(figsize=(8,5))
    plt.plot(lengths_all_a, times_all_a, 'r-o', label="All a's")
    plt.plot(lengths_random, times_random, 'b-o', label="Random {a,c,g,t}")
    plt.xlabel("String length (n)")
    plt.ylabel("Time (seconds)")
    plt.title(f"Suffix Array Construction Times (Sequential, First {args.num_files} Files)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("suffix_array_times_sequential.png", dpi=300)
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()

