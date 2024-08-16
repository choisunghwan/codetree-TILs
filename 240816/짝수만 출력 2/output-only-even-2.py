b , a = map (int,input().split())
temp = []

while a <= b:
    if a % 2 == 0:
        temp.append(a)

    a += 1

temp.sort(reverse = True)

print(" ".join(map(str, temp)))