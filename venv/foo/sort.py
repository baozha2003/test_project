import unittest


def sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums;


class Test(unittest.TestCase):
    def test_sort(self):
        nums = [22, 52, 11, 25, 825, 41, 26, 652, 852, 15, 151, 7]
        nums2 = [7, 11, 15, 22, 25, 26, 41, 52, 151, 652, 825, 852]
        # print(sort(nums))
        self.assertEquals(sort(nums),nums2)


if __name__ == '__main__':
    unittest.main()
