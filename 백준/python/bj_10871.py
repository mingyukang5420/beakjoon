N, X = map(int, input().split())

given_input = list(map(int, input().split()))

for item in given_input:
    if item < X:
        print(item, end=' ')
