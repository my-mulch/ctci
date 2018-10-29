from collections import defaultdict


def triple_step(n, memo):
    if n == 0:
        return 1

    if n < 0:
        return 0

    one_away = memo[n - 1] if memo[n - 1] else triple_step(n - 1, memo)
    two_away = memo[n - 2] if memo[n - 2] else triple_step(n - 2, memo)
    three_away = memo[n - 3] if memo[n - 3] else triple_step(n - 3, memo)

    memo[n] = one_away + two_away + three_away

    return memo[n]


def robot_walk(grid, paths, memo=defaultdict(bool), r=0, c=0):
    if r < 0 or c < 0 or not grid[r][c]:
        return False

    at_origin = (r == 0) and (c == 0)

    if (r, c) in memo:
        return memo[r, c]

    successful_path = False

    if at_origin or robot_walk(grid, paths, memo, r, c - 1) or robot_walk(grid, paths, memo, r - 1, c):
        paths.append((r, c))
        successful_path = True

    memo[(r, c)] = successful_path
    return successful_path