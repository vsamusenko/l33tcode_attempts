def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        print('list before pop:', nums)
        cur = nums.pop(i)
        print('list after pop:', nums)
        j = i-1
        print('i:',i,'cur:',cur,'j:',j)
        while j >=0 and nums[j] > cur:
            print('while loop cycle')
            j -= 1
        nums.insert(j+1, cur)
    return nums


x = [4, 2, 6, 3, 4, 6, 2, 1]
print(insertion_sort(x))