def dfs(n: int, cost: int) -> int:
    """
    dfs로 탐색하면서 최소비용을 계산
    Args:
        n (int): 현재 탐색이 몇 개월째인지
        cost (int): n개월차의 최소 비용
    Return:
        int: 최소 비용을 반환
    """
    global charges
    global plan
    global min_cost

    if min_cost < cost:
        return

    if n > 12:
        if min_cost > cost:
            min_cost = cost
        return min_cost

    dfs(n+1, cost + charges[0] * plan[n])  # n개월을 모두 일간권으로 지불
    dfs(n+1, cost + charges[1])  # n개월째에 월간권 지불
    dfs(n+3, cost + charges[2])  # n개월째에 분기권 지불
    dfs(n+12, cost + charges[3])  # n개월쨰에 연간권 지불


def get_input():

    charges = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan = [None] + plan  # 인덱스가 0인건 버리고 나머지 쓰려고

    return charges, plan


# def open_input_as_stdin():
    # import sys
    # sys.stdin = open("input_1952.txt")


# def main():
    # dfs(1, 0)


if __name__ == "__main__":
    # open_input_as_stdin()
    T = int(input())
    for tc in range(1, T+1):
        min_cost = 3000  # 연간 권이 3000인 경우
        charges, plan = get_input()
        dfs(1, 0)
        # main()
        print(f"#{tc} {min_cost}")