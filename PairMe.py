for i in range(int(input())):
    x, y, z = map(int, input().split())

    if x+y == z:
        print("YES")
    elif y+z == x:
        print("YES")
    elif x+z == y:
        print("YES")
    else:
        print("NO")