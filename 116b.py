n,m = input().split()
n = int(n)
m = int(m)
l=[]
l2 = []
for i in range(m+2):
    l2.append(".")

l.append(l2)
for i in range(n):
    s = input()
    s = "."+s+"."
    l1 = list(s)
    #l1.append(".")
    l.append(l1)
l.append(l2)
#print (l)
count=0
for i in range(1,n+1):
    for j in range(1,m+1):
        if l[i][j] == "W":
            if l[i+1][j] == "P" or l[i-1][j] == "P" or l[i][j+1] == "P" or l[i][j-1] == "P":
                count+=1

print (count)
