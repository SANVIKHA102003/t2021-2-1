a = int(input("Enter a positive integer: "))
if a > 0:
    output = ""
    for i in range(a):
        output += str(2 * i+1)
        if i < a - 1:
            output += ", "
    print(output)
else:
    print("Please enter a positive integer.")
