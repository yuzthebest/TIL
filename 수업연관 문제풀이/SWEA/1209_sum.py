import sys
sys.stdin = open("input.txt")


def get_max_num(mat):

    row_max_num = 0
    for row in mat:
        sum = 0
        for i in row:
            sum += i
        if sum > row_max_num:
            row_max_num = sum

    column_max_num = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += mat[j][i]
        if sum > column_max_num:
            column_max_num = sum

    daegak_max_sum = 0
    sum = 0
    for i in range(100):
        j = i
        sum += mat[i][j]
    if sum > daegak_max_sum:
        daegak_max_sum = sum

    sum = 0
    for i in range(100):
        j = 99-i
        sum += mat[i][j]
    if sum > daegak_max_sum:
        daegak_max_sum = sum

    return max(row_max_num, column_max_num, daegak_max_sum)



for tc in range(1,11):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]

    result = get_max_num(matrix)
    print(f'#{tc} {result}')