def RDS (nums):
    pH = nums[0]
    k = 1
    count = 0
    elecount = len(nums)
    while 1 <= k < len(nums):
        if pH == nums[k]:
            del(nums[k])
            count += 1
            k -= 1
            elecount -= 1
        pH = nums[k]
        k += 1
    for i in range(count):
        nums.append(None)
    return elecount


def RDS_Final (nums):
    if not nums:
        return 0
    nt = 0
    for i in range (1, len(nums)):
        if nums[i] != nums[nt]:
            nt += 1
            nums[nt] = nums[i]
    return nt + 1


if __name__ == '__main__':
    a = [1, 2, 2, 3, 3, 3, 3]
    print(RDS_Final(a))
