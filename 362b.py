"""

def clean_stairs(l,ans="NO"):
    if l[0] == 1 or l[n] == 1:
        return ans
    else:
        i=1
        while( i >=1 and i<=n):
            diff = n-i
            if diff == 0:
                ans = "YES"
                return ans
            else:
                if diff == 3:
                    i = i+3
                else:
                    if diff == 2:
                        i = i+2
                    else:
                        if diff == 1:
                            i = i+1
            if diff > 3:
                if l[i+3]!=1:
                    i = i+3
                else:
                    if l[i+2]!=1:
                        i = i+2
                    else:
                        if l[i+1]!=1:
                            i=i+1
                        else:
                            ans = "NO"
                            return ans

"""
n,m = raw_input().split()
n = int(n)
m = int(m)
#l = [0]*(n+1)
ans = "NO"
if m!=0:
    l1 = map(int,raw_input().split())
    #for i in l1:
    #    l[i] = 1
    #print l

    l1.sort()
    #print l1
    if l1[0] == 1 or l1[m-1] == n:
        ans = "NO"
    else:
        if m < 3:
            ans = "YES"
        else:
            for i in range(2,len(l1)):
                if l1[i]-l1[i-2] == 2:
                        ans = "NO"
                        break
                else:
                    ans = "YES"
else:
    ans  = "YES"




print ans
