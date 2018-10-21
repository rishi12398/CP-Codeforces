n = int(input())
d = dict()
l = list(map(int,input().split()))
l1=[]
for i in l:
    l1.append(i)
l1.sort()
count=0
for i in range(len(l1)):
    if l1[i] not in d:
        d[l1[i]]=[]
        count+=1

for i in range(len(l)):
    d[l[i]].append(i)
print (d)
#print (count)
count=0
dif=0
l2=[]
for key in d:
    if len(d[key])==1:
        count+=1
        l2.append((key,0))
    else:
        if len(d[key])==2:
            dif = d[key][1]-d[key][0]
            count+=1
            #print(key,dif)
            l2.append((key,dif))
        else:
            dif = d[key][1]-d[key][0]
            for i in range(2,len(d[key])):
                if (d[key][i]-d[key][i-1]) is not dif:
                    dif = 0
                    break
            if dif is not 0:
                count+=1
                #print(key,dif)
                l2.append((key,dif))

print (count)
for i in range(len(l2)):
    print(l2[i][0],l2[i][1])
