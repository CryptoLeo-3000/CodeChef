T = int(input())

for i in range(T):
    xa, xb, Xa, Xb = map(int, input().split())

    print(int(Xa/xa) + int(Xb/xb))