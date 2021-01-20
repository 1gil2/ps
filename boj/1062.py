#gold 4
#pypy3

import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global answer

    if cnt == k - 5:
        read_cnt = 0
        for word in words:
            for w in word:
                if not visit[ord(w) - ord('a')]:
                    break
            else:
                read_cnt += 1
        answer = max(answer, read_cnt)
        return

    for i in range(idx, 26):
        if not visit[i]:
            visit[i] = True
            dfs(i, cnt + 1)
            visit[i] = False

answer = 0
n, k = map(int, input().split())

if k < 5:
    print(0)
    sys.exit(0)
elif k == 26:
    print(n)
    sys.exit(0)

words = [set(input().rstrip()) for _ in range(n)]
visit = [False] * 26

visit[ord('a')-ord('a')] = True
visit[ord('c')-ord('a')] = True
visit[ord('i')-ord('a')] = True
visit[ord('n')-ord('a')] = True
visit[ord('t')-ord('a')] = True

dfs(0, 0)
print(answer)