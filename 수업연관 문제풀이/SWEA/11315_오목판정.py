import sys
sys.stdin = open("input.txt")

def is_omok(M, N):

    for row in M:
        total = 0
        for i in range(N):
            if row[i] == 'o':
                total += 1
                if total >= 5:
                   return 'YES'
            else:
                total = 0

    for i in range(N):
        total = 0
        for j in range(N):
            if M[j][i] == 'o':
                total += 1
                if total >= 5:
                    return 'YES'
            else:
                total = 0

    daegak_total = 0
    for i in range(N):
        j = i
        if M[i][j] == 'o':
            daegak_total += 1
            if daegak_total >= 5:
                return 'YES'
        else:
            daegak_total = 0

    g_total = 0
    for i in range(N):
        j = N-1-i
        if M[i][j] == 'o':
            g_total += 1
            if g_total >= 5:
                return 'YES'
        else:
            g_total = 0
    return 'NO'

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    matrix = [list(map(str, input())) for _ in range(N)]

    print(f'#{tc} {is_omok(matrix, N)}')