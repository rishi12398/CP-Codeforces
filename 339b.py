n,t = raw_input().split()
n = int(n)
t = int(t)
time = 0
start = 1
end = n
l = map(int,raw_input().split())
for dest in l :
    if start == dest:
        time = time
    else:
        if dest <= end and dest > start:
            time = time + (dest - start)
            start = dest
        else:
            if start > dest :
                time = time + (end - start) + dest
                start = dest
print time
