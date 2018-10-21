d,sum = input().split()
d = int(d)
sum = int(sum)
l=list()
for i in range(d):
    min,max = input().split()
    min = int(min)
    max = int(max)
    l.append((min,max))

#print (l)
max_sum=0
min_sum=0
for i in range(len(l)):
    max_sum += l[i][1]
    min_sum += l[i][0]
if max_sum < sum or min_sum > sum:
    print ("NO")
else:
    dist = [0]*d
    for i in range(len(l)):
        dist[i]=l[i][0]
        sum -= dist[i]

    #print (dist)
    #print (sum)
    i=0
    while sum!=0:
        if dist[i]+1 <= l[i][1]:
            dist[i]+=1
            sum-=1
            #print (dist)
        if i== d-1 and sum!=0:
            i=0
        else:
            i+=1
    print ("YES")
    for i in range(d):
        print (dist[i],end=" "),
