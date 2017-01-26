T = int(input("Enter the number of tests: "))

for x in range(T):
    I, F = map(int, input().split())
    count = 0
    while True:
        if I > F:
            I //= 2
            count += 1
        elif I < F:
            if F % I == 0:
                I *= 2
                count += 1
            else:
                I //= 2
                count += 1
        else:
            print(count)
            break