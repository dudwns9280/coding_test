def solution(nums):
    total_count = len(nums)
    nums_set = set(nums)

    if len(nums_set) >= total_count//2:
        return total_count//2
    else:
        return len(nums_set)