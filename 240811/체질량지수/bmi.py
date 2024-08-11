import math
h, w = map(int,input().split())


numerator = 10000 * w 
denominator = h*h

answer = numerator / denominator

answer1 = math.floor(answer)

# print(f'{b:.1f}')

print(answer1)

if answer1 >= 25 :
    print("Obesity")