a = int(input())
b = int(input())
c = int(input())

if (a <= b) and (b <= c):   # 1 2 3
    print(f"meio = {b}")
elif (c <= b) and (b <= a): # 3 2 1
    print(f"meio = {b}")
elif (b <= a) and (a <= c): # 2 1 3
    print(f"meio = {a}")
elif (c <= a) and (a <= b): # 2 3 1
    print(f"meio = {a}")
elif (a <= c) and (c <= b): # 1 3 2
    print(f"meio = {c}")
else:
    print(f"meio = {c}")    # 3 1 2