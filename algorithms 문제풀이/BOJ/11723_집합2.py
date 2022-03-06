import sys
sys.stdin = open("input.txt")

d = []

def get_result(func, num):
    global d
    if func == 'all':
        d = [i for i in range(1, 21)]
    elif func == 'empty':
        d = []
    else:
        if func == 'add':
            if num not in d:
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

T = int(sys.stdin.readline())

for tc in range(T):
    data = sys.stdin.readline().strip().split()
    if(len(data)) == 1:
        func = data[0]
        get_result(func, 0)
    else:
        func, num = data[0], int(data[1])
        get_result(func, num)



