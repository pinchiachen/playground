def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(0)
    less_arr = [num for num in arr if num < pivot]
    greater_arr = [num for num in arr if num >= pivot]
    return quick_sort(less_arr) + [pivot] + quick_sort(greater_arr)

if __name__ == "__main__":
    arr = [1, 3, 9, 2, 7, 5, 8, 6, 0, 4]
    print(quick_sort(arr))