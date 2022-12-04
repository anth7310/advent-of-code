## Part 1
max_val = 0
with open('input', 'r') as f:
    curr_val = 0
    lst = f.read().split('\n')
    for num in lst:
        if num == '':
            max_val = max(max_val, curr_val)
            curr_val = 0
        else:
            curr_val += int(num)
print(max(max_val, curr_val))

## Part 2
import heapq
h = []
with open('input', 'r') as f:
    curr_val = 0
    lst = f.read().split('\n')
    for num in lst:
        if num == '':
            heapq.heappush(h, curr_val)
            if len(h) > 3:
                heapq.heappop(h)
            curr_val = 0
        else:
            curr_val += int(num)
heapq.heappush(h, curr_val)
if len(h) > 3:
    heapq.heappop(h)
print(sum(h))
