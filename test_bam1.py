import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'group_8_data.txt'
data = pd.read_csv(file_path, sep=",")
data.columns = data.columns.str.strip()

# Prepare the data
try:
    offset = data['offset']
    avg_coverage = data['avg_coverage']
except KeyError as e:
    print(f"Column not found: {e}")
    exit()

# Number of bins
num_bins = 1000
samples_per_bin = len(offset) // num_bins

print(len(offset))
print("Samples per bin:", samples_per_bin)

# Binning the data and calculating the mean for each bin
binned_data = []
bin_start_values = []

for i in range(num_bins):
    start = i * samples_per_bin
    end = (i + 1) * samples_per_bin
    bin_avg_coverage = avg_coverage[start:end].mean()
    binned_data.append(bin_avg_coverage)
    bin_start_values.append(offset.iloc[start])

# Write the bin start and average coverage to a text file
output_file = 'binned_coverage_data.txt'
with open(output_file, 'w') as f:
    f.write("Bin_Start\tBin_Avg_Coverage\n")
    for bin_start, bin_avg in zip(bin_start_values, binned_data):
        f.write(f"{bin_start}\t{bin_avg}\n")

# Plotting the binned data
plt.figure(figsize=(12, 6))
plt.bar(bin_start_values, binned_data, width=(141213431 / num_bins), align='edge', edgecolor='steelblue')
plt.xlabel("Genomic Position (0 to 141,213,431)")
plt.ylabel("Average Coverage")
plt.title("Average Coverage for Binned Data (Chr 9)")
plt.xlim(0, 141213431)

# Show the plot
plt.show()


