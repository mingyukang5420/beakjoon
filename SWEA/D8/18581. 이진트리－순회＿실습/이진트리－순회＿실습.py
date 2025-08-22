def traverse_preorder(curr_node: int):
    """
    전위 순회로 돌아요 처리는 프린트만 슥삭
    Args:
        curr_node (int): 현재 노드 번호
    """
    global left_child
    global right_child
    # leaf_node에서 종료
    if curr_node is None:
        return

    left_node = left_child[curr_node]  # 좌측
    right_node = right_child[curr_node]   # 우측

    print(curr_node, end=' ')  # 왔으니까 찍어
    traverse_preorder(left_node)  # 좌측 재귀
    traverse_preorder(right_node)  # 우측 재귀


def traverse_inorder(curr_node: int):
    """
    중위 순회로 돌아요 처리는 프린트만 슥삭
    Args:
        curr_node (int): 현재 노드 번호
    """
    global left_child
    global right_child
    # leaf_node에서 종료
    if curr_node is None:
        return

    left_node = left_child[curr_node]  # 좌측
    right_node = right_child[curr_node]   # 우측

    traverse_inorder(left_node)  # 좌측 재귀
    print(curr_node, end=' ')  # 왔으니까 찍어
    traverse_inorder(right_node)  # 우측 재귀


def traverse_postorder(curr_node: int):
    """
    후위 순회로 돌아요 처리는 프린트만 슥삭
    Args:
        curr_node (int): 현재 노드 번호
    """
    global left_child
    global right_child
    # leaf_node에서 종료
    if curr_node is None:
        return

    left_node = left_child[curr_node]  # 좌측
    right_node = right_child[curr_node]   # 우측

    traverse_postorder(left_node)  # 좌측 재귀
    traverse_postorder(right_node)  # 우측 재귀
    print(curr_node, end=' ')  # 왔으니까 찍어


def get_tree_info(V: int) -> list:
    """
    트리 정보를 읽어와 반환
    Args:
        V (int): the number of vertex
    Returns:
        [left_child, right_child]
    """
    E = V - 1

    given_input = list(map(int, input().split()))

    left_child = [None for _ in range(V + 1)]
    right_child = [None for _ in range(V + 1)]

    for i in range(E):
        parent, child = given_input[2 * i], given_input[2 * i + 1]

        if left_child[parent]:  # 왼쪽이 먼저 채워진 경우
            right_child[parent] = child

        else:
            left_child[parent] = child

    return [left_child, right_child]


# def open_input_as_stdin():
    # import sys
    # sys.stdin = open("input_18581.txt")


def main():
    traverse_preorder(1)
    print()
    traverse_inorder(1)
    print()
    traverse_postorder(1)
    pass


if __name__ == "__main__":
    # open_input_as_stdin()
    V = int(input())
    result = get_tree_info(V)
    left_child = result[0]
    right_child = result[1]
    main()
