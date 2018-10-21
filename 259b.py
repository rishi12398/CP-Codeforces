l1 = map(int,raw_input().split())
l2 = map(int,raw_input().split())
l3 = map(int,raw_input().split())

sum = (l1[1]+l1[2]+l2[0]+l2[2]+l3[0]+l3[1])/2

l1[0] = sum - l1[1] - l1[2]
l2[1] = sum - l2[0] - l2[2]
l3[2] = sum - l3[0] - l3[1]

for i in range(len(l1)):
    print str(l1[i]),

print

for i in range(len(l2)):
    print str(l2[i]),

print

for i in range(len(l3)):
    print str(l3[i]),
