n=input()
a=list(map(int,raw_input().split()))
l,ans=0,2
if n>1 else 1
for i in range(2,n):
    if a[i]==a[i-1]+a[i-2]:
        ans=max(ans,i-l+1)
    else :
        l=i-1
print ans
