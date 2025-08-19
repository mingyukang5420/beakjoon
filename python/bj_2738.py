N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

result = [[0 for _ in range(M)] for _ in range(N)]

for row in range(len(A)):
    for col in range(len(A[0])):

        result[row][col] = A[row][col] + B[row][col]

for row in result:
    print(*row)
