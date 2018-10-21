n,k = raw_input().split()
n = int(n)
k = int(k)
s = raw_input()
l = list(s)
l1=[]
l.sort()
#print l
l1.append(l[0])
j=0
for i in range(1,len(l)):
    if (((ord(l[i])-96) - (ord(l1[j])-96) != 1) and ((ord(l[i])-96) - (ord(l1[j])-96) != 2) ):
        l1.append(l[i])
        #print l[i]

        j+=1
        #print j
print l1
if len(l1) == k:
    sum = 0
    for i in range(len(l1)):
        sum = sum + (ord(l1[i])-96)
else:
    sum = -1

print sum
