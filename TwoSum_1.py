def TwoSum (nums, target):
    for i in range (len(nums)):
        for k in range (i, len(nums)):
            if nums[k] + nums [i] == target and k != i:
                return i, k


def TwoSum_1 (nums, target):
    db = {0: nums[0]}
    for i in range(1, len(nums)):
        if nums[i] ==

if __name__ == '__main__':
    nums = [5, 3, 2, 4]
    print(TwoSum(nums, 6))