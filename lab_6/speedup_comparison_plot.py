import matplotlib.pyplot as plt

modes = ["Sequential", "Process (load)", "Process (no)", "Thread"]
times = [4.388, 3.917, 3.71, 16.243]
speedup = [4.388/x for x in times]

plt.bar(modes, speedup, color=["red", "blue", "green", "purple"])
plt.ylabel("Speedup")
plt.title("Speedup Comparison")
plt.show()
