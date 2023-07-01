# AB

# 정수 N과 K가 주어졌을 때, 다음 두 조건을 만족하는 문자열 S를 찾는 프로그램을 작성하시오.

# 문자열 S의 길이는 N이고, 'A', 'B'로 이루어져 있다.
# 문자열 S에는 0 ≤ i < j < N 이면서 s[i] == 'A' && s[j] == 'B'를 만족하는 (i, j) 쌍이 K개가 있다.

# 입력
# 첫째 줄에 N과 K가 주어진다. (2 ≤ N ≤ 50, 0 ≤ K ≤ N(N-1)/2)

# 출력
# 첫째 줄에 문제의 조건을 만족하는 문자열 S를 출력한다. 가능한 S가 여러 가지라면, 아무거나 출력한다. 만약, 그러한 S가 존재하지 않는 경우에는 -1을 출력한다

def solution():
    n,k = map(int,input().split())

    a = 0
    b = n
    while a*b < k and b > 0:
        a += 1
        b -= 1

    if k == 0:
        return 'B'*n
    elif b == 0:
        return -1

    remain = k - (a-1)*b

    return 'A'*(a-1) + 'B'*(b-remain) + 'A' + 'B'*remain

print(solution())