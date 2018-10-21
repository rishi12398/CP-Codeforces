"""def no_of_steps(r,x,y,x1,y1):
    x2 = abs(x-x1)
    y2 = abs(y-y1)
    steps = 0
    while(1):
        if x2 == 0 and y2 == 0:
            #print steps
            break
        else:
            if x2 > 0 and y2 > 0:
                if x2 > y2:
                    steps = steps+y2
                    x2 = x2-y2
                    y2=0
                else:
                    if y2 > x2:
                        steps = steps + x2
                        y2 = y2-x2

                        x2=0
                    else:
                        steps = steps + x2
                        x2=0
                        y2=0
                #print steps
                #print "$"
            else:
                #print "#"
                if x2 == 0 and y2%(2*r)==0:
                    #y2 = y2 - 2*r
                    #print "hi"
                    steps =steps+ y2/(2*r)
                    y2 = 0
                else:
                    if x2%(2*r)==0 and y == 0:
                        #print "hello"
                        steps = steps+x2/(2*r)
                        x2=0


    return steps

"""
import math
r,x,y,x1,y1 = raw_input().split()
r = int(r)
y = int(y)
x = int(x)
x1 = int(x1)
y1 = int(y1)
d= math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))
print int(math.ceil(d/(2*r)))
