import sys
sys.stdin = open("input.txt")

T = int(sys.stdin.readline())
s = []

for tc in range(T):
    data = sys.stdin.readline().strip().split()

    if len(data) == 1:
        if data[0] == 'all':
            s = [i for i in range(1, 21)]
        else:
            s = []
    else:
        func = data[0]
        num = int(data[1])
        if func == 'add':
            if num not in s:
                s.append(num)
        elif func == 'remove':
            if num in s:
                index = s.index(num)
                del s[index]
        elif func == 'check':
            print(1 if num in s else 0)
        elif func == 'toggle':
            if num in s:
                index = s.index(num)
                del s[index]
            else:
                s.append(num)