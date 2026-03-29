def make_strings_equal(s: str, t: str) -> tuple:
    n = len(s)
    cnt = {}
    
    # Count occurrences of 'a' and 'b' in both strings
    for i in range(n):
        if s[i] not in cnt:
            cnt[s[i]] = 1
        else:
            cnt[s[i]] += 1
        if t[i] not in cnt:
            cnt[t[i]] = 1
        else:
            cnt[t[i]] += 1
    
    # Check if the total count of 'a' and 'b' is even
    for key in cnt:
        if cnt[key] % 2 != 0:
            return -1, []
    
    ans = []
    ff = deque([])
    ss = deque([])
    
    # Identify positions where characters differ
    for i in range(n):
        if s[i] == t[i]:
            continue
        if s[i] == 'a' and t[i] == 'b':
            ff.append(i + 1)
        else:
            ss.append(i + 1)
    
    # Perform swaps to make the strings equal
    while len(ff) > 1:
        t1 = ff.popleft()
        t2 = ff.popleft()
        ans.append((t2, t1))
    
    while len(ss) > 1:
        t1 = ss.popleft()
        t2 = ss.popleft()
        ans.append((t1, t2))
    
    if len(ff) > 0:
        t1 = ff.popleft()
        t2 = ss.popleft()
        ans.append((t2, t2))
        ans.append((t1, t2))
    
    return len(ans), ans