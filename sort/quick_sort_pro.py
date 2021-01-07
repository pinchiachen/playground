## Use median of medians to find pivot and avoid the worst case of quick sort
def quick_sort_pro(arr):
    if len(arr) <= 1:
        return arr
    pivot = find_pivot(arr)
    less_arr = []
    greater_arr = []
    for num in arr:
        if num < pivot:
            less_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
    return quick_sort_pro(less_arr) + [pivot] + quick_sort_pro(greater_arr)

def find_pivot(arr):
    div_arrs = []
    for num in arr:
        if not div_arrs or len(div_arrs[-1]) == 5:
            div_arrs.append([num])
        else:
            div_arrs[-1].append(num)
    medians = [find_median(sorted(div_arr)) for div_arr in div_arrs]
    median_of_medians = find_median(medians)
    return median_of_medians

def find_median(arr):
    return arr[len(arr)//2]

def main():
    arr = [14, 1, 13, 3, 9, 12, 2, 7, 5, 8, 15, 6, 0, 16, 4, 10, 11]
    print(quick_sort_pro(arr))

if __name__ == "__main__":
    main()