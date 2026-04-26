def find3Numbers(arr):

    if len(arr) < 3:
        return []

    i = 0
    new_arr = []

    while i < len(arr):

        if new_arr and new_arr[-1] < arr[i]:
            new_arr.append(arr[i])
        elif len(new_arr) == 0:
            new_arr.append(arr[i])

        i += 1

    return new_arr


print(find3Numbers([12, 11, 10, 5, 6, 2, 30]))
