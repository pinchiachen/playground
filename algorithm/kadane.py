## Kadane Algorithm is used to solve Maximum Subarray Problem
def kadane(nums):
    max_sum = 0
    cur_sum = 0
    for num in nums:
        # choose keeping cur_sum or starting a new cur_sum
        cur_sum = max(cur_sum + num, num)
        # save the max cur_sum so far
        max_sum = max(max_sum, cur_sum)
    return max_sum

if __name__ == "__main__":
    nums = [-2, 1, 3, -2, 1, 4, -5, 1]
    print(kadane(nums))