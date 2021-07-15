N = int(input())

for i in range(10):
    if N % (10-i) == 0:
        print(10-i)
        break