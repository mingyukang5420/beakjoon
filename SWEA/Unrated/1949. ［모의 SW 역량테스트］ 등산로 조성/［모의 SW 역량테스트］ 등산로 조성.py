# 1949
def dfs(r: int, c: int, prev_height: int, length: int, has_chance: bool):
    """
    Args:
        r (int) : current_row
        c (int) : current_col
        prev_height (int) : previous_height
        length (int) : current path length
        has_chance (bool) : flag indicating if cutting is still available
    """
    global ans
    ans = max(ans, length)

    # 종료조건 - 탐색 끝난 경우

    # 방문행동 - 없음

    # 재귀호출
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] is False:
            nh = arr[nr][nc]

            # 그냥 갈 수 있는 경우
            if nh < prev_height:
                visited[nr][nc] = True
                dfs(nr, nc, nh, length + 1, has_chance)
                visited[nr][nc] = False

            # 찬스를 써서 깎는 경우
            for k in range(1, K+1):  # 공사 높이는 유동적
                if has_chance and nh - k < prev_height:
                    visited[nr][nc] = True
                    dfs(nr, nc, nh - k, length + 1, False)  
                    visited[nr][nc] = False
                    # nh - k : 실제 깎아서 이동한 높이


def get_max(arr: list):
    maximum = 0
    for row in arr:
        for item in row:
            if item > maximum:
                maximum = item
    return maximum


def get_index(arr: list, element: int):
    result = []
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == element:
                result.append((row, col))
    return result


T = int(input())

dr = [-1, +1, +0, +0]
dc = [+0, +0, -1, +1]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    max_height = get_max(arr)
    start_idx = get_index(arr, max_height)
    visited = [[False] * N for _ in range(N)]

    for sr, sc in start_idx:  # start_row, start_col
        visited[sr][sc] = True
        dfs(sr, sc, arr[sr][sc], 1, True)
        visited[sr][sc] = False

    print(f"#{tc} {ans}")


set().intersection