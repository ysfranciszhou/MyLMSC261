x = int(input("Enter the tall(1~8) of pyramid: "))
y = 2*x - 2
if x > 0 and x < 9:
    for m in range(0, x):
        for n in range(0, y):
            print(end=" ")
        y = y - 2
        for n in range(0, m+1):
            print("# ", end="")
        print("\r")
else:
    print("The number is out of range, please exit the program and try again.")
