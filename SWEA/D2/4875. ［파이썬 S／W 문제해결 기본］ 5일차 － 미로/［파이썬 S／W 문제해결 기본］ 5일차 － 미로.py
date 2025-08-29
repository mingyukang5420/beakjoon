# 4875 - DFS

def get_start_point(matrix: list) -> tuple:
    """
    주어진 배열에서 시작점이 어딘지 반환하는 함수
    """
    n = len(matrix)
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "2":
                return row, col


def dfs(cr, cc):
    global ans
    # 종료조건 - 조기종료

    # 종료조건 - 정답처리
    if arr[cr][cc] == "3":
        ans = 1
        return

    # 방문 행동 - nothing to do

    # 재귀 호출 - 전처리
    for idx in range(4):
        nr = cr + dr[idx]
        nc = cc + dc[idx]

        # 재귀 호출

        # 경계검사와 벽이 아닌지, 미방문인지 체크
        if 0 <= nr < N and 0 <= nc < N \
                and arr[nr][nc] != "1" and visited[nr][nc] is False:
            visited[nr][nc] = True
            dfs(nr, nc)


# 델타 : 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]

    start_row, start_col = get_start_point(arr)
    # goal_row, goal_col = get_goal_point(arr)

    visited = [[False] * N for _ in range(N)]

    visited[start_row][start_col] = True  # 초기 방문 처리
    ans = 0
    dfs(start_row, start_col)

    print(f"#{tc} {ans}")
