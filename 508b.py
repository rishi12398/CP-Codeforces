def largest(l):
    #print "#"
    count = False
    min = 99999
    j=0
    last = l[len(l)-1]
    for i in range(len(l)):
        if l[i]%2 == 0 and l[i] < last:
            #print "#"
            #print l[i]
            temp = l[i]
            l[i] = l[len(l)-1]
            l[len(l)-1] = temp
            count = True
            return l

        if l[i]%2 == 0 and l[i] > last:
            if j <= i:
                min = l[i]
                j=i
            count = True

    if count == False:
        return []
    temp = l[j]
    l[j] = l[len(l)-1]
    l[len(l)-1] = temp
    return l

n = raw_input()
l = list(n)

for i in range(len(l)):
    l[i] = int(l[i])

l1 = largest(l)

for i in range(len(l1)):
    l1[i] = str(l1[i])
if len(l1):
    print "".join(l1)
else:
    print "-1"
