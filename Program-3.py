a = int(input("Enter a positive integer: "))
if a > 0:
    output = ""
    for i in range(a+1):
        if i%2 !=0:
            output += str(i)
            if i < a - 1:
                output += ", "
    print(output)
else:
    print("Please enter a positive integer.")
