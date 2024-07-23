import matplotlib.pyplot as plt

# Create a figure and a single subplot
fig, ax = plt.subplots()

# Plot some data on the subplot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
ax.plot(x, y, 'b-', label='Prime Numbers')

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Plot')
ax.legend()

# Display the plot
plt.show()
