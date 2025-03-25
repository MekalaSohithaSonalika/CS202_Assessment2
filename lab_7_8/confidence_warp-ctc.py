import matplotlib.pyplot as plt

# Data from the results (for warp-ctc; since warp-ctc & Pokemon-Go-Controller are the same, one example is enough)
labels = ["HIGH Confidence", "MEDIUM Confidence", "LOW Confidence"]
confidence_counts = [577, 15, 1]
colors = ["blue", "purple", "gray"]

plt.figure(figsize=(6, 6))
plt.pie(confidence_counts, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})

plt.title("Issue Confidence Distribution (warp-ctc)")
plt.show()
