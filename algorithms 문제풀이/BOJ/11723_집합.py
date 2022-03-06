import sys
sys.stdin = open("input.txt")

T = int(sys.stdin.readline())

d = []

for tc in range(T):
    data = sys.stdin.readline().strip().split()
    if(len(data)) == 1:
        if data[0] == 'all':
            d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        else:
            d =[]
    else:
        func, num = data[0], int(data[1])
        if func == 'add':
            if num in d:
                pass
            else:
                d.append(num)
        if func == 'remove':
            if num in d:
                d.remove(num)
        if func == 'check':
            if num in d:
                print(1)
            else:
                print(0)
        if func == 'toggle':
            if num in d:
                d.remove(num)
            else:
                d.append(num)




