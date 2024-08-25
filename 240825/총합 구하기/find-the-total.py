a , b = map(int, input().split())
answer = 0 

for num in range(a, b+1):
    # print(num)
    if num % 6 == 0 and num % 8 != 0 :
        # print(num)
        answer += num
print(answer)