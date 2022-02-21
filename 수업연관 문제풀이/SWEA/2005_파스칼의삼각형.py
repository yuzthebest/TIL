import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    matrix = [[] for _ in range(N)]

    for i in range(N):
        matrix[i].append(1)
        for j in range(1, i+1):
            if i == 1:
                matrix[i].append(1)
            else:
                if j != i:
                    matrix[i].append(matrix[i-1][j-1] + matrix[i-1][j])
                else:
                    matrix[i].append(1)
    print(f'#{tc}')
    for i in matrix:
        print(' '.join(map(str, i)))

