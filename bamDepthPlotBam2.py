import matplotlib.pyplot as plt
import numpy as np

data = {}
current_key = None

with open("readDepth.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("#"):
            # Extract the key
            current_key = line[1:]
            data[current_key] = []
        elif current_key is not None and line and not line.startswith("*"):
            # Extract offset, reads and calculate avgCoverage
            parts = line.split()
            offset = int(parts[0])
            reads = int(parts[1])
            avg_coverage = reads / 16384
            data[current_key].append([offset, reads, avg_coverage])

# Select data for group #4
group_data = data.get("8", [])

# Write group_4_data to a file
with open("group_8_data.txt", "w") as f:
    f.write("offset, reads, avg_coverage\n")
    for offset, reads, avg_coverage in group_data:
        f.write(f"{offset}, {reads}, {avg_coverage:.6f}\n")

# # Write the entire data dictionary to a file
# with open("all_data.txt", "w") as f:
#     for key, values in data.items():
#         f.write(f"# {key}\n")
#         f.write("offset, reads, avg_coverage\n")
#         for offset, reads, avg_coverage in values:
#             f.write(f"{offset}, {reads}, {avg_coverage:.6f}\n")
#         f.write("\n")

# Set up binning parameters
x_start = 0
x_end = 180915260
num_bins = 1000

# Create bins and initialize avgCoverage sums
bin_edges = np.linspace(x_start, x_end, num_bins + 1)
bin_sums = np.zeros(num_bins)
bin_counts = np.zeros(num_bins)

# Aggregate data into bins
for offset, _, avg_coverage in group_data:
    bin_index = np.searchsorted(bin_edges, offset, side='right') - 1
    if 0 <= bin_index < num_bins:
        bin_sums[bin_index] += avg_coverage
        bin_counts[bin_index] += 1

# Calculate average coverage per bin
bin_avg_coverage = np.divide(bin_sums, bin_counts, out=np.zeros_like(bin_sums), where=bin_counts != 0)

# Calculate overall average coverage from the original data
overall_avg_coverage = np.mean([avg_coverage for _, _, avg_coverage in group_data])

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(range(num_bins), bin_avg_coverage, width=1.0, label='Average Coverage per Bin')
plt.axhline(y=overall_avg_coverage, color='r', linestyle='--', linewidth=2, label='Overall Average Coverage')

# Add y tick for the overall average coverage
yticks = plt.yticks()[0]
plt.yticks(list(yticks) + [overall_avg_coverage], labels=list(yticks) + [f"Overall Avg: {overall_avg_coverage:.2f}"])

plt.xlabel("Bins (0 to 180,915,260)")
plt.ylabel("Average Coverage")
plt.title("Average Coverage for Group #4")
plt.legend()
plt.show()


