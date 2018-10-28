

def get_perms(arr, all_perms=[], cur_perm=[]):
    if not arr:
        all_perms.append(cur_perm.copy())
        return

    for i in range(len(arr)):
        cur_perm.append(arr[i])
        get_perms(arr[:i] + arr[i + 1:], all_perms, cur_perm)
        cur_perm.pop()

    return all_perms.copy()
