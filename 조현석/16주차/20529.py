# 가장 가까운 세 사람의 심리적 거리

def diff(A, B):
    cnt = 0
    for i in range(4):
        if A[i] != B[i]:
            cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    N = int(input())
    types = input().split()
    min = 1000000000
    if N > 32:
        print(0)
        continue
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                t = diff(types[i], types[j]) + diff(types[j], types[k]) + diff(types[k], types[i])
                if t < min:
                    min = t
    print(min)
