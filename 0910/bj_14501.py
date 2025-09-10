import sys

sys.stdin = open("input_14501.txt")


def dfs(time_list, pay_list, day, profit, best, pass_today):
    # 종료조건 - 정답상황
    if day > N:  # 출근하는 날 이상이면
        if best < profit:  # best 최대값 갱신
            best = profit
            return best

    # 방문행동 - 없음

    # 재귀 호출
    curr_profit = pay_list[day]
    profit += curr_profit

    if pass_today:
        next_day = day + 1
    else:
        next_day = day + time_list[day]

    dfs(time_list, pay_list, next_day, profit, best, True)
    dfs(time_list, pay_list, next_day, profit, best, False)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    time_list = [1]  # 0일에 대한 정보 패딩
    pay_list = [0]

    for _ in range(N):
        t, p = map(int, input().split())

        time_list.append(t)
        pay_list.append(p)

    ans = dfs(time_list, pay_list, 0, 0, 0, True)
    result = dfs(time_list, pay_list, 0, 0, 0, False)
    ans = max(ans, result)

    print(f"#{tc} {ans}")
