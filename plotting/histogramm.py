import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]
# data = [10, 15, 10, 15, 18, 18, 20, 25, 30]
#
# plt.hist(data, bins=5, color='purple', edgecolor='black')
# plt.title("Histogram Example")
# plt.xlabel("Bins")
# plt.ylabel("Frequency")
# plt.show()
plt.plot(x, y, label="Line 1")
plt.plot(x, [15, 10, 12, 14, 15], label="Line 2")
plt.legend()  # Display the legend
plt.show()

