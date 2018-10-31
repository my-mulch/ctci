

def get_perms(arr, all_perms=[], cur_perm=[]):
    if not arr:
        all_perms.append(cur_perm.copy())
        return

    for i in range(len(arr)):
        cur_perm.append(arr[i])
        get_perms(arr[:i] + arr[i + 1:], all_perms, cur_perm)
        cur_perm.pop()

    return all_perms.copy()


def binary_search(arr, key):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        print(mid)

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            low = mid + 1

        if arr[mid] > key:
            high = mid - 1

    return -1  # miss
