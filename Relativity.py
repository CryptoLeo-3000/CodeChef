T = int(input())

for i in range(T):
    g, c = map(int, input().split())
    print(int((c * c)/(2*g)))