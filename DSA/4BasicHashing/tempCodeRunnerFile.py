# Creating an array of size N+1
N = 5
frequency = [0] * (N + 1)  # An array with 6 slots: [0, 0, 0, 0, 0, 0]

# If we have an array like this: [2, 3, 5, 3, 2, 5, 0]
arr = [2, 3, 5, 3, 2, 5, 0]

# Count the frequency of each number in the array
for num in arr:
    frequency[num] += 1
    print(frequency,"\n \n")

# Now, let's see the frequency array
print(frequency)
