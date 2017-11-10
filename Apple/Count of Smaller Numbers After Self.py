class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ## method, insert sort, from the last element in the array, the index of the insert location is the number of less number
        ## the search using the binary search
        sorted_arr = []
        res = []
        for i in range(len(nums)-1, -1, -1):
            idx = self.searchLoc(sorted_arr, nums[i])
            res.append(idx)
            sorted_arr.insert(idx, nums[i])
        res.reverse()
        return res
    def searchLoc(self, arr, val):
        if len(arr) == 0:
            return 0
        else:
            l , r = 0, len(arr)-1
            while l <=r:
                mid = (l+r)/2
                if arr[mid] > val and (arr[mid-1]< val or mid-1 < 0):
                    return mid
                elif arr[mid]>= val:
                    r = mid-1
                else:
                    l = mid+1
            return l

sol = Solution()
print sol.countSmaller([-1,-1,-1])