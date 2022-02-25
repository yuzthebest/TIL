import sys
sys.stdin = open("input.txt")

garo, sero = map(int, input().split())
store_nums = int(input())

store_matrix = [list(map(int, input().split())) for _ in range(store_nums)]

dong_direct, dong_block = map(int, input().split())

distance = 0
distance2 = 0
distance3 = 0

for i in range(store_nums):
    # 같은 x값 선상에 위치
    if store_matrix[i][0] == dong_direct:
        distance += abs(store_matrix[i][1]-dong_block)
    # 바로 맞은편 선상에 위치
    elif store_matrix[i][0] + dong_direct == 3 or store_matrix[i][0] + dong_direct == 7:
        # dong_direct가 세로일때
        if dong_direct == 3 or dong_direct == 4:
            if store_matrix[i][1] + dong_block > sero:
                distance2 += (2*sero - store_matrix[i][1] - dong_block + garo)
            else:
                distance2 += (store_matrix[i][1] + dong_block + garo)
        # dong_direct가 가로일때
        else:
            if store_matrix[i][1] + dong_block > garo:
                distance2 += (2*garo - store_matrix[i][1] - dong_block + sero)
            else:
                distance2 += (store_matrix[i][1] + dong_block + sero)
    # 인접변에 위치한경우
    else:
        if store_matrix[i][0] == 1:
            if dong_direct == 3:
                distance3 += (dong_block + store_matrix[i][1])
            else:
                distance3 += (dong_block + garo - store_matrix[i][1])
        elif store_matrix[i][0] == 2:
            if dong_direct == 3:
                distance3 += (sero - dong_block + store_matrix[i][1])
            else:
                distance3 += (sero - dong_block + garo - store_matrix[i][1])
        elif store_matrix[i][0] == 3:
            if dong_direct == 1:
                distance3 += (dong_block + store_matrix[i][1])
            else:
                distance3 += (dong_block + sero - store_matrix[i][1])
        else:
            if dong_direct == 2:
                distance3 += (garo - dong_block + sero - store_matrix[i][1])
            else:
                distance3 += (garo - dong_block + store_matrix[i][1])

print(f'{distance + distance2 + distance3}')


