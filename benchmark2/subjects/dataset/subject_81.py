def find_min_number(N: str, d: str) -> str:
    a = list(N)
    w = int(d)
    count = 1
    l = []
    
    while True:
        if count != len(a):
            count = 1
            for i in range(len(a) - 1):
                if int(a[i]) > int(a[i + 1]):
                    a.pop(i)
                    a.append(d)
                    break
                else:
                    count += 1
        else:
            for i in range(len(a)):
                if int(a[i]) >= w:
                    l.append(a[i])
                    a.append(d)
                elif int(a[i]) == w:
                    break
            break
    
    for i in l:
        a.remove(i)
    
    return ''.join(a)