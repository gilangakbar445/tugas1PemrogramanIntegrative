total = 0
while True:
    x = int(input("Enter number : "))
    if x == int(-1):
        break
    number = int(x)
    total += number
print(total)