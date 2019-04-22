a = int(input('Enter your age: '))
i = 0
while i <= (a - 2):
    if a%2 == 0:
        i = i + 2
        print(i)
    elif a%2 == 1:
        i = 0
        while i <= a:
            i = i + 2
            print(i-1)