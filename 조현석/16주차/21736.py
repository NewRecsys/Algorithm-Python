#	헌내기는 친구가 필요해

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
def dfs(x, y):
    global cnt
    if board[x][y] == 'P':
        cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and board[nx][ny] != 'X':
            dfs(nx, ny)

for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            dfs(i, j)
if cnt == 0:
    print('TT')
else:
    print(cnt)