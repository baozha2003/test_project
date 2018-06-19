def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j+1],nums[j]
                print(nums)
        print("")

nums = [232321,99,102,412,13,43,21,65,312,54,87,123,322,412,42357,870]
bubbleSort(nums)
