import matplotlib.pyplot as plt

# Data from results
repositories = ["warp-ctc", "grade", "Pokemon-Go-Controller"]
cwe_counts = [593, 593, 593]

plt.figure(figsize=(8, 5))
plt.bar(repositories, cwe_counts, color="teal")

plt.ylabel("Total CWE Occurrences")
plt.xlabel("Repositories")
plt.title("CWE Category Distribution Across Repositories")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()
