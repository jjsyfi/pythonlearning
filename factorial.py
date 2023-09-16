num = int(input("Please type in a number:"))
i = 1
result = 1
while i <= num:
    if num <= 0:
        print("Thanks and bye")
    else:
        result *= i
        print(f"The factorial of number {num} is {result}")
    i += 1#need a loop for the input