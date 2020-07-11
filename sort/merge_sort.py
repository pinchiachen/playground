def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        l = 0
        r = 0
        index = 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] <= right_arr[r]:
                arr[index] = left_arr[l]
                l += 1
            else:
                arr[index] = right_arr[r]
                r += 1
            index += 1
        while l < len(left_arr):
            arr[index] = left_arr[l]
            l += 1
            index += 1
        while r < len(right_arr):
            arr[index] = right_arr[r]
            r += 1
            index += 1
    return arr

if __name__ == "__main__":
    arr = [1, 3, 9, 2, 7, 5, 8, 6, 0, 4]
    print(merge_sort(arr))
