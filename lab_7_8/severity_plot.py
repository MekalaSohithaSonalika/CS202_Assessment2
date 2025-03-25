import matplotlib.pyplot as plt
import numpy as np

# Data from the results
repositories = ["warp-ctc", "grade", "Pokemon-Go-Controller"]
high_severity = [17, 5, 17]
medium_severity = [36, 9, 36]
low_severity = [540, 136, 540]

# Bar width
bar_width = 0.2  
x = np.arange(len(repositories))

# Creating the bar chart
plt.figure(figsize=(8, 5))
plt.bar(x - bar_width, high_severity, width=bar_width, label="HIGH", color="red")
plt.bar(x, medium_severity, width=bar_width, label="MEDIUM", color="orange")
plt.bar(x + bar_width, low_severity, width=bar_width, label="LOW", color="green")

plt.xticks(ticks=x, labels=repositories)
plt.ylabel("Number of Issues")
plt.xlabel("Repositories")
plt.title("Issue Severity Distribution Across Repositories")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
