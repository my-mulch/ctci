
def triple_step(n, memo=[]):
    memo.extend([1, 1, 2])
    
    for i in range(3, n + 1):
        memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3])

    return memo[n]
