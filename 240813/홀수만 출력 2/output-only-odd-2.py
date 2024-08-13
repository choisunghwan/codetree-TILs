b , a = map(int, input().split())
num = []
for i in range(a, b+1):
    if i % 2 == 1:
        num.append(str(i))
num.sort(reverse = True)
print(" ".join(map(str,num)))