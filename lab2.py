import math

piles = list(map(int, input('input piles: ').split()))
h = int(input('input hours: '))

def bananas_in_hours(piles,k):
    hours = 0
    for p in piles:
        hours += math.ceil(p/k)
    return hours
    
def binar_search(piles,h):
    l = 1
    r = max(piles)
    result = 0
    while l <= r:
        mid = (l + r )// 2 
        if bananas_in_hours(piles,mid) <= h:
            result = mid 
            r = mid - 1
        else:
            l = mid +1 
    return result
    
print(f'Minimum speed K: {binar_search(piles, h)}')