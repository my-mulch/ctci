"""  
Nums is an array containing all ints 0 ... len(nums)

But missing one!
"""


def find_missing(nums, column=0):
    if len(nums) == 1:
        return nums.pop() ^ (1 << column)

    zeros = []
    ones = []

    for num in nums:
        group = ones if num & (1 << column) else zeros
        group.append(num)

    return find_missing(ones if len(ones) < len(zeros) else zeros, column + 1)
