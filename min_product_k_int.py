import heapq as min_heap

def min_product_of_k_int(l,k,pro=1):
    min_heap.heapify(l)
    #print (l)
    while k!=0:
        i = min_heap.heappop(l)
        pro = pro*i
        k-=1
    return pro

l = list(map(int,input().split()))
k = int(input())
print(min_product_of_k_int(l,k))
