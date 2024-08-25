a , b = map(int,input().split())
answer = 1 

for num in range(1, b+1):
    if num % a == 0 :
        answer *= num
print(answer)