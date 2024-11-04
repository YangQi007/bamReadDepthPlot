# import pysam
# import matplotlib.pyplot as plt


# bamfile = pysam.AlignmentFile("NA12878.exome.bam", "rb")

# # Calculate the depth for chromosome
# depth = [pileupcolumn.n for pileupcolumn in bamfile.pileup("11")]

# # Calculate the average depth
# average_depth = sum(depth) / len(depth)

# # Plot the depth and add the average line
# plt.plot(depth, label="Read Depth")
# plt.axhline(average_depth, color='red', linestyle='--', label=f"Average Depth: {average_depth:.2f}")
# plt.ylabel("Read Depth")
# plt.title("Read Depth Plot with Average Coverage on Chromosome 11")
# plt.legend()
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Define parameters
desired_num_bins = 1000
chromosome_length = 141213431  # Length of chromosome in base pairs
new_bin_size = chromosome_length / desired_num_bins  # Calculate new bin size

print(f"new_bin_size: {new_bin_size}")

# Read the depth data from the file
depths = []
positions = []

with open('depth9.txt', 'r') as file:
    for line in file:
        _, position, depth = line.strip().split()
        positions.append(int(position))
        depths.append(int(depth))

# Convert depths and positions to numpy arrays for easier processing
depths = np.array(depths)
positions = np.array(positions)


#Calculate average depth for each new bin, including the remainder at the end
binned_depth = []
for i in range(desired_num_bins):
    start = int(i * new_bin_size)
    end = int((i + 1) * new_bin_size)
    end = min(end, chromosome_length)  # Make sure not to exceed chromosome length

    # Get depth values within the current bin range
    mask = (positions >= start) & (positions < end)
    bin_depth_values = depths[mask]
    if len(bin_depth_values) > 0:
        binned_depth.append(np.mean(bin_depth_values))
    else:
        binned_depth.append(0)

# Calculate the overall average depth across the entire chromosome
overall_average_depth = np.mean(binned_depth)

# Generate genomic position labels for the x-axis (start position of each bin)
x_labels = [int(i * new_bin_size) for i in range(desired_num_bins)]


# Plot the binned depth as a bar chart and add the overall average line
plt.figure(figsize=(12, 6))  # Set the figure size for better visualization
plt.bar(x_labels, binned_depth, width=new_bin_size, align="edge", label="Binned Average Read Depth", alpha=0.7)
plt.axhline(overall_average_depth, color='red', linestyle='--', label=f"Overall Average Depth: {overall_average_depth:.2f}")
plt.xlabel("Position on Chromosome 5 (Base Pairs)")
plt.ylabel("Average Read Depth")
plt.title(f"Binned Read Depth Bar Chart (Grouped into {desired_num_bins} Bins) with Overall Average Coverage on Chromosome 5")

# Add number of bins to the chart
num_bins = len(binned_depth)
plt.text(0.95, 0.95, f'Number of Bins: {num_bins}', horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
plt.legend()
plt.tight_layout()
plt.show()


# Write the bin's x-axis and mean(bin_depth_values) into a file
# output_file = "binned_depth_output9.txt"

# with open(output_file, "w") as file:
#     # Write a header line
#     file.write("Bin_Start_Position\tAverage_Depth\n")
    
#     # Iterate over x_labels and binned_depth and write them to the file
#     for i in range(len(binned_depth)):
#         bin_start = x_labels[i]
#         avg_depth = binned_depth[i]
#         file.write(f"{bin_start}\t{avg_depth:.2f}\n")

# print(f"Binned depth data has been written to {output_file}")


