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