a, b = map(int, input().split())
temp = []

for _ in range(b):
    if a <= 0:
        print(0)
    else:
        temp.append(a)

print("".join(map(str,temp)))