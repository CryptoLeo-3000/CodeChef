A, B, C = map(int, input().split())

if A == B:
    print("YES")
elif B == C:
    print("YES")
elif C == A:
    print("YES")
else:
    print("NO")