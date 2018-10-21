def maximum_value_sum(l,arr_sum,curr):
    max_value = curr
    for i in range(1,len(l)):
        curr = curr + arr_sum - len(l)*l[len(l)-i]
        if curr > max_value:
            max_value = curr

    return max_value

l = map(int,raw_input().split())
arr_sum = 0
curr = 0
for i in range(len(l)):
    arr_sum = arr_sum + l[i]
    curr = curr + i*l[i]
print maximum_value_sum(l,arr_sum,curr)    
