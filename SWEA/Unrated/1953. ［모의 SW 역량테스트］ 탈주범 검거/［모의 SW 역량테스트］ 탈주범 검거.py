from collections import deque
 
def bfs(row, col) -> int:
    """ 시작지점을 넣으면 숨을 수 있는 곳 계산
    """
    # 변수 초기화
    visited = [[0] * M for _ in range(N)]
    # 방문한 곳 개수 세기
    ans = 0
 
    # 초기 시작 처리
    queue = deque()
    queue.append((row, col))
 
    # 시작 지점을 방문 처리
    visited[row][col] = 1
     
    # 방문한 곳 개수
    ans += 1
 
    # 큐가 빌 때까지 반복
    while queue:
        # 반복을 시작하면 바로 꺼내기
        curr_row, curr_col = queue.popleft()
         
        # 현재 파이프의 종류: 1 ~ 7
        curr_pipe = arr[curr_row][curr_col]
 
        # 거리에 다다르면 종료
        if visited[curr_row][curr_col] == L:
            return ans
         
        for direction in range(4):  # 상하좌우 델타 이동
            next_row = curr_row + dr[direction]
            next_col = curr_col + dc[direction]
 
 
 
            # 경계검사
            # 방문 안 한곳
            # 델타 이동 가능한 곳인지
            # 도착지점이 연결 되어 있는지
            if 0 <= next_row < N and 0 <= next_col < M \
                and visited[next_row][next_col] == 0:
                 
                # 다음 파이프 종류: 0 ~ 7
                next_pipe = arr[next_row][next_col]
 
                if pipe[curr_pipe][direction] == 1 \
                and pipe[next_pipe][(5 - direction) % 4] == 1:
 
                    # 큐에 추가하기
                    queue.append((next_row, next_col))
 
                    # 방문 배열에 길이를 기록하기
                    visited[next_row][next_col] = visited[curr_row][curr_col] + 1
 
                    # 숨을 곳 늘리기
                    ans += 1
 
    return ans
 
 
T = int(input())
 
# 파이프 번호 별 연결된 곳 표시, 순서대로 상하좌우
# 0번 인덱스는 패딩용
pipe = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],
        [1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
 
# 순서대로 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
     
    result = bfs(R, C)
 
    print(f"#{tc} {result}")