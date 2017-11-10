def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sum = 0
    sub = 0
    for i in range(len(nums)):
        sub += nums[i]
        ## being silly
        sum = max(sum, sub)
        if sub < 0:

            sub = 0

    return sum
arr1 = [ -5, 4, 3, -1, 3, -20, 2, 3]
arr = [ -5, 4, 3, -1, 3, -1, 2, 3]
print maxSubArray(arr1)
print maxSubArray(arr)
