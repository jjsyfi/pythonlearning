num = 6#int(input("Please type in a number:"))
i = 1
j = 2
while i <= num:
    print(j)
    print(i)
    i += 2
    if num % 2 != 0 and i == num:
        print(i)
        break
    else:
        j += 2