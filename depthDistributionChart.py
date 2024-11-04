# I have a depth file calulated from the bam file. I want to plot the depth distribution of a chromosome.

# The depth file is in the format:
# 13	19240777	1
# 13	19240778	1
# 13	19240779	3
# 13	19240780	4
# 13	19240781	5
# 13	19240782	5
# 13	19240783	6
# 13	19240784	6
# 13	19240785	9
# 13	19240786	10

# The first column is the chromosome number, the second column is the position on the chromosome, and the third column is the depth at that position.

# Draw the distribution of the depth of chromosome 13. 
# The x-axis should be the depth, and the y-axis should be the percentage of the depth in the all data of the depth file.
import matplotlib.pyplot as plt
import numpy as np

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

# Calculate the total number of positions
total_positions = len(positions)

# Calculate the unique depths and their counts
unique_depths, depth_counts = np.unique(depths, return_counts=True)

# Calculate the percentage of each depth
depth_percentages = (depth_counts / total_positions) * 100

# Plot the depth distribution
plt.figure(figsize=(12, 6))
plt.bar(unique_depths, depth_percentages, color='steelblue')
plt.xlabel("Depth")
plt.ylabel("Percentage of Depth")
plt.title("Depth Distribution of Chromosome 11")
plt.show()

