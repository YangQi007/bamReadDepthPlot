# import matplotlib.pyplot as plt
# import pandas as pd

# # Load the data from group_4_data.txt
# data = pd.read_csv("group_4_data.txt")

# # Print the column names to verify if there's any issue
# print(data.columns)

# # Rename columns to remove any leading/trailing spaces if needed
# data.columns = data.columns.str.strip()

# # Plot the bar chart based on correct column names
# plt.figure(figsize=(12, 6))
# plt.bar(data['offset'], data['avg_coverage'], width=16384, align='edge')

# # Set chart labels and title
# plt.xlabel("Genomic Position (0 to 180,915,260)")
# plt.ylabel("Average Coverage")
# plt.title("Average Coverage for Each Offset (Group #4)")

# # Show the plot
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data from group_4_data.txt
data = pd.read_csv("group_8_data.txt")

# Rename columns to remove any leading/trailing spaces if needed
data.columns = data.columns.str.strip()

# Set up binning parameters
x_start = 0
x_end = 141213431
num_bins = 1000
bin_size = (x_end - x_start) / num_bins

# Create bins and initialize avgCoverage sums
bin_edges = np.linspace(x_start, x_end, num_bins + 1)
data['bin'] = pd.cut(data['offset'], bins=bin_edges, labels=False, include_lowest=True)

# Calculate average coverage for each bin
binned_avg_coverage = data.groupby('bin')['avg_coverage'].mean().fillna(0)

# Ensure that x_positions and binned_avg_coverage have the same length
x_positions = bin_edges[:-1][:len(binned_avg_coverage)]

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(x_positions, binned_avg_coverage, width=1, align='edge', edgecolor='steelblue')

# Set chart labels and title
plt.xlabel("Genomic Position (0 to 180,915,260)")
plt.ylabel("Average Coverage")
plt.title("Average Coverage for Binned Data (Chr 9)")
plt.show()
