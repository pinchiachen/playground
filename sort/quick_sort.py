def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(0)
    less_arr = []
    greater_arr = []
    for num in arr:
        if num < pivot:
            less_arr.append(num)
        else:
            greater_arr.append(num)
    return quick_sort(less_arr) + [pivot] + quick_sort(greater_arr)

if __name__ == "__main__":
    arr = [1, 3, 9, 2, 7, 5, 8, 6, 0, 4]
    print(quick_sort(arr))