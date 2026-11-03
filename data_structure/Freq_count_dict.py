# Question: Write a Python program to count the frequency
# of each element in a list using a dictionary.

def count_frequency(numbers):
    frequency = {}

    for n in numbers:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1

    return frequency


data = [10, 20, 10, 30, 20, 10, 40]

result = count_frequency(data)

for num, count in result.items():
    print(num, "appears", count, "times")
