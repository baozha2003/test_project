def sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums;


nums = [22, 52, 11, 25, 825, 41, 26, 652, 852, 15, 151, 7]
print(sort(nums))
