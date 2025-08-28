def dfs(cr: int, cc: int, dir_: int, visited: list):
    """
    문제 조건에 따른 DFS 탐색
    Args:
        cr (int): 현재 지점의 row - current_row
        cc (int): 현재 지점의 column - current_column
        dir_ (int): 진행방향 0 - 우상, 1 - 우하, 2 - 좌하, 3 - 좌상
        visited (list[int]): 방문한 곳의 디저트 번호를 저장
    """
    global arr
    global ans

    # 종료조건 구역
        # 조기 종료 - 한바퀴 돌고 또 돌때
    if dir_ > 3:
        return

    # 종료 조건
        # 정답 처리 - 한바퀴 다 돌고 복귀
    if dir_ == 3 and (sr, sc) == (cr, cc):
        ans = max(ans, len(visited))
        return

    # 방문처리 구역 - 할 것 없음

    # 다음 호출 구역

        # 다음 호출을 위한 전처리
    for diagonal in [dir_, dir_ + 1]:
        nr = cr + dr[diagonal]
        nc = cc + dc[diagonal]

        # 다음 호출
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] not in visited:
            visited.append(arr[nr][nc])
            dfs(nr, nc, diagonal, visited)
            visited.pop()  # 백트래킹


T = int(input())

dr = [-1, +1, +1, -1, -1]
dc = [+1, +1, -1, -1, +1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for sr in range(1, N-1):
        for sc in range(N-2):
            dfs(sr, sc, 0, [])

    print(f"#{tc} {ans}")
