T = int(input())

for i in range(T):
    n = input()
    count = 0
    for j in n:
        if j == '4':
            count += 1
    
    print(count)