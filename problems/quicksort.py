import random
import sys
def quick_sort(nums, s,e):
    if s <e:
        pivot = part(nums, s,e)
        quick_sort(nums,s, pivot-1)
        quick_sort(nums, pivot+1, e)

def part(nums, s,e):

    idx = random.randint(s, e)
    nums[idx], nums[s] = nums[s], nums[idx]
    pivot = nums[s]
    small = s
    for i in range(s+1,e+1):
        if nums[i] < pivot:
            small += 1
            nums[small], nums[i] = nums[i], nums[small]

    nums[small], nums[s] = nums[s], nums[small]
    return small

def quickSortVersion2(nums):
    if len(nums) == 0:
        return []
    idx = random.randint(0, len(nums)-1)
    small = [i for i in nums if i < nums[idx]]
    equ = [i for i in nums if i == nums[idx]]
    large = [i for i in nums if i > nums[idx]]
    small = quickSortVersion2(small)
    large = quickSortVersion2(large)
    return small+equ+large


def main():
    nums = [10,1,2, 6,3,7,8,8,4,10]
    quick_sort(nums, 0, len(nums)-1)
    print nums
    nums2 = [10,1,2]
    print quickSortVersion2(nums)

if __name__ == "__main__":
    main()