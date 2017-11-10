class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        counter = 0
        curr = -1
        c_1, c_2 = 0, 0
        total_l = len(nums1) + len(nums2)
        idx1, idx2 = -1, -1
        n1, n2 = -1, -1
        if total_l % 2 == 0:
            idx1 = total_l / 2
            idx2 = idx1 - 1
        else:
            idx1 = int(total_l / 2)
        tmp = -1
        while counter != idx1 and c_1 <= len(nums1) and c_2 <= len(nums2):
            if counter == idx2:
                n2 = tmp
            if nums1[c_1] < nums2[c_2]:
                tmp = nums1[c_1]
                c_1 += 1

            else:
                tmp = nums2[c_2]
                c_2 += 1
            counter += 1
        if counter < idx1:
            if c_1 == len(nums1):
                if idx2 != -1 and n2 != -1:
                    n2 = nums2[idx2 - counter + c_2]
                n1 = nums2[idx1 - counter + c_2]
            else:
                if idx2 != -1 and n2 != -1:
                    n2 = nums1[idx2 - counter + c_1]
                n1 = nums1[idx1 - counter + c_1]
        else:
            n1 = max(nums1[c_1], nums2[c_2])

        if n2 == -1:
            return n1
        else:
            return float(n1 + n2) / 2

    def findMedianSortedArrays2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        line  = []
        total_l = len(nums1) + len(nums2)
        idx1, idx2 = -1, -1
        n1, n2 = -1, -1
        if total_l % 2 == 0:
            idx1 = total_l / 2
            idx2 = idx1 - 1
        else:
            idx1 = int(total_l / 2)
        while len(nums1)>0 and len(nums2)>0:
            if nums1[0] < nums2[0]:
                line.append(nums1[0])
                nums1 = nums1[1:]
            else:
                line.append(nums2[0])
                nums2 = nums2[1:]
            if len(line)-1 >= idx1:
                if idx2 != -1:
                    return float(line[idx1] + line[idx2]) / 2
                else:
                    return line[idx1]
        if len(nums1)!= 0:
            line +=nums1
        else:
            line += nums2

        if idx1 < len(line):
            if idx2 != -1:
                return float(line[idx1]+line[idx2])/2
            else:
                return line[idx1]





sol = Solution()
print sol.findMedianSortedArrays2([1,3,4],[2])





