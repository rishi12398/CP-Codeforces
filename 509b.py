def painting_pebles(n,k,l,ans="NO"):
    maximum = max(l)
    minimum = min(l)
    diff = maximum - minimum
    if diff > k :
        ans = "NO"
        print ans
    else:
        ans = "YES"
        print ans
        for i in range(len(l)):
            #l1 = [0]*l[i]
            c = 1
            for j in range(l[i]):
                if c == k+1:
                    c=1
                print str(c),
                c+=1
            print


n,k = raw_input().split()
n = int(n)
k = int(k)
l = map(int,raw_input().split())
painting_pebles(n,k,l)
