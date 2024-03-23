n = 5
for r in range(1,11,2):
    for c in range(1,n):
        print(' ', end='')
    for r1 in range(r):
        print('*',end='')
    n = n-1
    print('\n')
