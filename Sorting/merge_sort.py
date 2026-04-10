
def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)


def merge(left_arr: list, right_arr: list):
    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result.extend(left_arr[i:])
    result.extend(right_arr[j:])

    return result


a = [2, 3, 1, 12, 2, 9, 5, 4]

print(merge_sort(a))


