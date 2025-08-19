import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for tc in range(1, T+1):
    input = lambda: sys.stdin.readline().rstrip()
    a, b = map(int, input().split())
    print(a + b)
