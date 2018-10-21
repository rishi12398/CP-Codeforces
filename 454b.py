n = input()
l = map(int,raw_input().split())
l1 = []


for i in range(len(l)):
    l1.append(l[i])


max = l1[0]
m=0
count = 0
for i in range(1,len(l1)):
    if l1[i] >= max :

        max = l1[i]
        m=i

    if l[i]!=max:
        break
l.sort()

#print max
#print m
shifts = (len(l)-1)-m
#m1 = (len(l)-1)-m
for i in range(len(l)-1,-1,-1):
    #print m
    if l1[m] != l[i]:
        shifts = -1
        break
    shifts = shifts
    if m == 0:
        m = len(l)-1
    else:
        m=m-1

print shifts
