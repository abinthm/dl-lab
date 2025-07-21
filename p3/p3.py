import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 6]

plt.plot(x, y, marker='o')        # Line plot with points
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig('line_plot_output.png', dpi=300, bbox_inches='tight')  # Save the plot
plt.show()