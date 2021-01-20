from ..utils.cal_run_time import calculate_run_time
from ..sort.quick_sort import quick_sort
from ..sort.quick_sort_pro import quick_sort_pro

def build_edge_test_data():
    arr = [i for i in range(800)]
    return arr

@calculate_run_time
def quick_sort_test(arr):
    return quick_sort(arr)

@calculate_run_time
def quick_sort_pro_test(arr):
    return quick_sort_pro(arr)

def main():
    test_arr = build_edge_test_data()
    print('---Start quick sort---')
    quick_sort_test(test_arr)
    print('---End quick sort---')
    test_arr = build_edge_test_data()
    print('---Start quick sort pro---')
    quick_sort_pro_test(test_arr)
    print('---End quick sort pro---')

if __name__ == "__main__":
    main()