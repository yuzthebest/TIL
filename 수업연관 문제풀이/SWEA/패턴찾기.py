
def is_pattern(y,x):
    for i in range(2):
        for j in range(2):
            if pattern[i][j] != matrix[i+y][j+x]:
                return 0
    return 1


matrix = [['A', 'B', 'G', 'K'],
          ['T', 'T', 'A', 'B'],
          ['A', 'C', 'C', 'D']]

pattern = [list(input()) for _ in range(2)]

result = 0
for i in range(2):
    for j in range(3):
        if is_pattern(i,j):
            result += 1

if result>=1:
    print('존재함')
else:
    print('존재하지않음')


