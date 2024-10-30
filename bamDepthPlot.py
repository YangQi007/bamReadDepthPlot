# import pysam
# import matplotlib.pyplot as plt


# bamfile = pysam.AlignmentFile("NA12878.exome.bam", "rb")

# # Calculate the depth for chromosome
# depth = [pileupcolumn.n for pileupcolumn in bamfile.pileup("X")]

# # Calculate the average depth
# average_depth = sum(depth) / len(depth)

# # Plot the depth and add the average line
# plt.plot(depth, label="Read Depth")
# plt.axhline(average_depth, color='red', linestyle='--', label=f"Average Depth: {average_depth:.2f}")
# plt.ylabel("Read Depth")
# plt.title("Read Depth Plot with Average Coverage on Chromosome X")
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Define parameters
# bin_size = 16384
# chromosome_length = 51304566  # Length of chromosome 22 in base pairs

# # Read the depth data from the file
# depths = []
# positions = []

# with open('depth22.txt', 'r') as file:
#     for line in file:
#         _, position, depth = line.strip().split()
#         positions.append(int(position))
#         depths.append(int(depth))

# # Convert depths and positions to numpy arrays for easier processing
# depths = np.array(depths)
# positions = np.array(positions)

# # Calculate average depth for each bin
# binned_depth = []
# for i in range(0, chromosome_length, bin_size):
#     # Get depth values within the current bin range
#     mask = (positions >= i) & (positions < i + bin_size)
#     bin_depth_values = depths[mask]
#     if len(bin_depth_values) > 0:
#         binned_depth.append(np.mean(bin_depth_values))
#     else:
#         binned_depth.append(0)

# # Calculate the overall average depth across the entire chromosome
# overall_average_depth = np.mean(binned_depth)

# # Generate genomic position labels for the x-axis (start position of each bin)
# x_labels = [i for i in range(0, len(binned_depth) * bin_size, bin_size)]

# # Plot the binned depth as a bar chart and add the overall average line
# plt.figure(figsize=(12, 6))  # Set the figure size for better visualization
# plt.bar(x_labels, binned_depth, width=bin_size, align="edge", label="Binned Average Read Depth", alpha=0.7)
# plt.axhline(overall_average_depth, color='red', linestyle='--', label=f"Overall Average Depth: {overall_average_depth:.2f}")
# plt.xlabel("Position on Chromosome 22 (Base Pairs)")
# plt.ylabel("Average Read Depth")
# plt.title("Binned Read Depth Bar Chart with Overall Average Coverage on Chromosome 22")

# # Add number of bins to the chart
# num_bins = len(binned_depth)
# plt.text(0.95, 0.95, f'Number of Bins: {num_bins}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

# plt.legend()
# plt.tight_layout()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Define parameters
desired_num_bins = 1000
chromosome_length = 135006516  # Length of chromosome in base pairs
new_bin_size = chromosome_length // desired_num_bins  # Calculate new bin size

# Read the depth data from the file
depths = []
positions = []

with open('depth11.txt', 'r') as file:
    for line in file:
        _, position, depth = line.strip().split()
        positions.append(int(position))
        depths.append(int(depth))

# Convert depths and positions to numpy arrays for easier processing
depths = np.array(depths)
positions = np.array(positions)

# Calculate average depth for each new bin
binned_depth = []
for i in range(0, chromosome_length, new_bin_size):
    # Get depth values within the current bin range
    mask = (positions >= i) & (positions < i + new_bin_size)
    bin_depth_values = depths[mask]
    if len(bin_depth_values) > 0:
        binned_depth.append(np.mean(bin_depth_values))
    else:
        binned_depth.append(0)

# Calculate the overall average depth across the entire chromosome
overall_average_depth = np.mean(binned_depth)

# Generate genomic position labels for the x-axis (start position of each bin)
x_labels = [i for i in range(0, len(binned_depth) * new_bin_size, new_bin_size)]

# Plot the binned depth as a bar chart and add the overall average line
plt.figure(figsize=(12, 6))  # Set the figure size for better visualization
plt.bar(x_labels, binned_depth, width=new_bin_size, align="edge", label="Binned Average Read Depth", alpha=0.7)
plt.axhline(overall_average_depth, color='red', linestyle='--', label=f"Overall Average Depth: {overall_average_depth:.2f}")
plt.xlabel("Position on Chromosome 11 (Base Pairs)")
plt.ylabel("Average Read Depth")
plt.title(f"Binned Read Depth Bar Chart (Grouped into {desired_num_bins} Bins) with Overall Average Coverage on Chromosome 11")

# Add number of bins to the chart
num_bins = len(binned_depth)
plt.text(0.95, 0.95, f'Number of Bins: {num_bins}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

plt.legend()
plt.tight_layout()
plt.show()

