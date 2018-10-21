n,m = input().split()
n = int(n)
m = int(m)
a = list(map(int,input().split()))
b = list(map(int,input().split()))
setb = set()
for i in range(len(b)):
    if b[i] not in setb:
        setb.add(b[i])
max_a = max(a)
max_b = max(b)
count=0
new = 0
#print (max_a)
#print (max_b)
if max_b <= max_a:
    for i in a:
        if i in setb:
            count+=1


else:
    count_greater = 0
    #print ("#")
    for i in range(len(b)):
        if b[i] > max_a:
            count_greater+=1
    #print (count_greater)
    for i in a:
        if i in setb:
            count+=1
        else:
            if i not in setb and count_greater!=0:
                count+=1
                count_greater-=1


#print (count)
new = n-count
print (new)
