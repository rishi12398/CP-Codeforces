n = input()
l=[]
for i in range(0,n):
    h = input()
    l.append(h)

#print l

time = l[0]+1
#print time


for i in range(1,len(l)):
    eats = 0
    jumps = 0
    climbs = 0
    if l[i] > l[i-1]:
        jumps+=1
        climbs = l[i] - l[i-1]
        eats+=1
        time = time + jumps + climbs + eats
        #print "time "+str(time)
    else:
        if l[i] < l[i-1]:
            climbs = l[i-1]-l[i]
            jumps+=1
            eats+=1
            time = time + jumps + climbs + eats
            #print "time "+str(time)
        else:
            jumps+=1
            eats+=1
            time = time + jumps + eats

print time
