T = int(input())

for i in range(T):
    X, A, B = map(int, input().split())
    print((A + ((100 - X) * B)) * 10)