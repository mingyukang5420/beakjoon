idx = 4
while idx > 0:
    idx -= 1
    star = '*'*(2*idx+1)
    space = ' '*(3-idx)

    print(f"{''.join([space, star])}")
