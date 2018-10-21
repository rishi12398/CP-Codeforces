n=int(input())
L=[]
for i in range(n):
    a,b=map(int,input().split())
    L.append((b,a))
L.sort(reverse=True)
ans=0
c=1
ind=0
while(c!=0 and ind<n):
    ans+=L[ind][1]
    c+=L[ind][0]-1
    ind+=1
print(ans)
