T = int(input())

for i in range(T):
    x, m, d = map(int, input().split())

    print(min(x*m, x+d))