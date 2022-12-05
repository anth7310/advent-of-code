# part 1
with open('input', 'r') as f:
    points = 0
    score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    for row in f.read().split('\n'):
        a, b = row.split()
        points += score[b]
        if a == 'A' and b == 'X' or a == 'B' and b == 'Y' or a == 'C' and b == 'Z':
            points += 3
        elif a == 'A' and b == 'Y' or a == 'B' and b == 'Z' or a == 'C' and b == 'X':
            points += 6
    print(points)

# part 2
with open('input', 'r') as f:
    points = 0
    for row in f.read().split('\n'):
        a, b = row.split()
        condition = {
            # lose
            'X': {'A': 3, 'B': 1, 'C': 2}, 
            # tie
            'Y': {'A': 1 + 3, 'B': 2 + 3, 'C': 3 + 3},
            # win
            'Z': {'A': 2 + 6, 'B': 3 + 6, 'C': 1 + 6},
        }
        points += condition[b][a]
    print(points)