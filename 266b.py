n,t = raw_input().split()
n = int(n)
t = int(t)
a = raw_input()
l = list(a)
for i in range(0,t):
    j=1
    while(j<n):
        if (l[j-1] == "B" and l[j] == "G"):
            temp = l[j-1]
            l[j-1] = l[j]
            l[j] = temp
            
            j=j+1
        j+=1

print "".join(l)
