person1 = input().split()
person2 = input().split()

if (int(person1[0]) >= 19 and person1[1] == 'M' or int(person2[0]) >= 19 and person2[1] == 'M' ):
    print(1)
else:
    print(0)