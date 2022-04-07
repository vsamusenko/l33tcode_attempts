from itertools import combinations

def twoSum(nums, target: int):
    if len(nums) > 2:

        for num in nums:
            first_num = num
            second_num = target - num
            if first_num == second_num:
                try:
                    return [nums.index(first_num), nums.index(second_num, nums.index(first_num)+1)]
                except:
                    continue
            else:
                if second_num in nums:
                    return [nums.index(first_num), nums.index(second_num)]


    else:
        return [0, 1]







print(twoSum([3,2,4], 6))

