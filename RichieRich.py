T = int(input())

for i in range(T):
    A, B, X = input().split()

    print(int((float(B)-float(A))/float(X)))