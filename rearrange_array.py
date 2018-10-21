def rearrange(l):
    hash = set()
    for i in range(len(l)):
        hash.add(l[i])

    for i in range(len(l)):
        if i in hash:
            l[i] = i
        else:
            l[i] = -1

    return l

l = map(int,raw_input().split())
print rearrange(l)
