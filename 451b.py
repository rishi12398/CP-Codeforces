n=input()
l1 = map(int,raw_input().split())
l=[]
for i in range(len(l1)):
    l.append(l1[i])
l1.sort()
l_sorted = l1
#print l
#print l_sorted
i=start=0
j=end=len(l)-1

for i in range(0,len(l)):
    if l[i] != l_sorted[i]:
        start = i
        break

for j in range(len(l)-1,-1,-1):
    if l[j] != l_sorted[j]:
        end = j
        break
#print start
#print end
ans = "yes"
if l == l_sorted:
    start=0
    end=0
    ans = "yes"
else:
    k=start
    #print start
    #print k
    i=0
    while(k <= end ):


        if l[k] != l_sorted[end-i]:
            #print i
            ans = "no"
            break
        i = i+1
        k = k+1
if ans == "no":
    print ans
else:
    print ans
    print str(start+1)+" "+str(end+1)
