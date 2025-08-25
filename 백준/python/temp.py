import itertools

def get_hit_order():
    """
    선수들의 모든 타순 경우를 반환
    1번 선수는 항상 4번타자
    => 8!가지 경우의 수
    """
    other_players = [i for i in range(2, 10)]
    all_permutations = list(itertools.permutations(other_players))

    all_hitting_orders = []
    for perm in all_permutations:
        order = list(perm)
        order.insert(3, 1)  # 1번 선수를 4번 타자(인덱스 3)로 삽입
        all_hitting_orders.append(order)

    return all_hitting_orders

def baseball_game(hitting_order: list, player_performance: list) -> int:
    """
    타순과, 선수들의 이닝 별 타석 결과가 있을 때 점수를 반환
    Args:
        hitting_order (list[int]): 타순
        player_performance (list[int]): 선수들의 이닝 별 타석 결과
    Returns:
        int: 타순대로 타석에 섰을때 점수 반환
    """
    score = 0
    curr_hitter_idx = 0
    end_inning = len(player_performance)

    for inning in range(end_inning):
        out_count = 0
        base_status = [0, 0, 0]  # 1루, 2루, 3루 주자 여부 (0: 없음, 1: 있음)

        while out_count < 3:
            hitter_player_num = hitting_order[curr_hitter_idx]
            hit_result = player_performance[inning][hitter_player_num - 1]

            if hit_result == 0:  # 아웃
                out_count += 1
            else:  # 안타, 2루타, 3루타, 홈런
                # 모든 주자와 타자 진루
                bases_after = [0, 0, 0]
                runs_scored = 0

                # 주자 진루
                for i in range(3):
                    if base_status[i] == 1:
                        new_pos = i + hit_result
                        if new_pos >= 3:
                            runs_scored += 1
                        else:
                            bases_after[new_pos] = 1

                # 타자 진루
                hitter_pos = hit_result - 1
                if hitter_pos >= 3:
                    runs_scored += 1
                else:
                    bases_after[hitter_pos] = 1

                # 병살타로 인한 주자 중복 방지를 위해 OR 연산
                new_bases = [0,0,0]
                new_bases[0] = bases_after[0] or base_status[0]
                new_bases[1] = bases_after[1] or base_status[1]
                new_bases[2] = bases_after[2] or base_status[2]

                base_status = new_bases
                score += runs_scored
            
            curr_hitter_idx = (curr_hitter_idx + 1) % 9

    return score


def open_input_as_stdin():
    import sys
    sys.stdin = open("input_17281.txt")


def main():
    N = int(input())
    given_input = [list(map(int, input().split())) for _ in range(N)]

    all_hitting_orders = get_hit_order()
    max_score = 0

    for order in all_hitting_orders:
        current_score = baseball_game(order, given_input)
        if current_score > max_score:
            max_score = current_score

    print(max_score)

if __name__ == "__main__":
    open_input_as_stdin()  # 파일 입력을 사용할 경우 주석 해제
    main()