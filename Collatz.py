def collatz(n):
    if n % 2 == 0:
        n = n / 2
    else:
        n = (3 * n) + 1
    return n


while True:
    try:
        number = int(input("Pick a number: "))
        break
    except ValueError:
        print("Not an integer")
print(number)

while True:
    if number != 1:
        number = (collatz(number))
        print(number)
    else:
        break


