n = input()
r = n%3
d = n/3
if r is 0 and d%3==0:
    a = d-1
    b = d-1
    c = d+2
else:
    if r is 0 and d%3!=0:
        a = d
        b = d
        c = d
    else:
        if r!=0 and d%3==0:
            a = d-1
            b = d-2
            c = d+3+r
        else:
            if r!=0 and d%3!=0:
                if (d+r)%3==0:
                    a=d
                    b=r
                    c=2*d
                else:
                    a=d
                    b=d
                    c=d+r



print str(a)+" "+str(b)+" "+str(c)
