n,m = raw_input().split()
n = int(n)
m = int(m)
l = [0 for i in range(0,m)]

l1 = l
n1 = n
def max_pair(l,n):
    max_pairs=0
    for i in range(len(l)):
        l[i]=l[i]+1
        n=n-1
    l[0] = l[0]+n
    max_pairs = ((l[0])*(l[0]-1))/2
    return max_pairs

def min_pair(l,n):
    min_pairs = 0
    i=0
    while n!=0:
        l[i] = l[i]+1
        n=n-1
        if i == len(l)-1:
            i=0
        else:
            i+=1
    for i in range(len(l)):
        if l[i] >= 2:
            min_pairs = min_pairs + ((l[i])*(l[i]-1))/2
        else:
            min_pairs = min_pairs

    return min_pairs

s1 = min_pair(l,n)
l = [0 for i in range(0,m)]
s2=max_pair(l,n)
print str(s1)+" "+str(s2)
