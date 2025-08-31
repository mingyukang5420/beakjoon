# 1949

def dfs(r, c, prev_height, length, has_chance):
    global ans
    ans = max(ans, length)

    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] is False:
            nh = arr[nr][nc]

            # 그냥 갈 수 있는 경우
            if nh < prev_height:
                visited[nr][nc] = True
                dfs(nr, nc, nh, length+1, has_chance)
                visited[nr][nc] = False

            # 찬스를 써서 깎는 경우
            for k in range(1, K+1):
                if has_chance and nh - k < prev_height:
                    visited[nr][nc] = True
                    dfs(nr, nc, nh-k, length+1, False)  
                    visited[nr][nc] = False
                    # prev_height-1 : 실제 깎아서 이동한 높이


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
