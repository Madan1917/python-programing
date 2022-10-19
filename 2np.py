if _ _name_ _ == '_ _main_ _':
    T = int(input())
    E = list(map(int,
input().split()))
    L = list(map(int,
input().split()))
    current_presence = 0
    max_presence = 0
    for i in range(T):
        current_presence +=
E[i] - L[i]
        if max_presence<
current_presence:
            max_presence =
current_presence
    print (max_presence, end =
'')
    
