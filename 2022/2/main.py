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