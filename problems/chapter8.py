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


def magic_index(arr, left, right):
    if right < left:
        return -1

    mid_index = (left + right) // 2
    mid_value = arr[mid_index]

    if mid_value == mid_index:
        return mid_index

    left_side = magic_index(arr, left, min(mid_index - 1, mid_value))

    if left_side >= 0:
        return left_side

    right_side = magic_index(arr, max(mid_index + 1, mid_value), right)

    return right_side


def power_set(arr, working_set=[], sets=[]):
    if not arr:
        sets.append(working_set.copy())
        return

    power_set(arr[1:], [arr[0]] + working_set, sets)
    power_set(arr[1:], working_set, sets)

    return sets


def recursive_multiply(a, b):
    if not a:
        return 0

    return recursive_multiply(a - 1, b) + b


def recursive_multiply_fast(a, b):
    smaller = a if a < b else b
    bigger = a if a > b else b
    return recursive_multiply_fast_helper(smaller, bigger)


def recursive_multiply_fast_helper(smaller, bigger):
    if smaller == 0:
        return 0

    if smaller == 1:
        return b

    half_product = recursive_multiply_fast_helper(smaller >> 1, bigger)

    return half_product + half_product + bigger if smaller % 2 else 0
