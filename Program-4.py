numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
multiple= {}
for i in range(1, 10):
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    multiple[i] = count
print(multiple)
