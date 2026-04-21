'''
There a couple of ways to attack this problem: hashMap (O(n)) or sorting (Olg(n)) approach. I'll go over the
sorting approach. We can sort the array from ascending order. This will allow the use of two pointers: i and j
i gets incremented if nums[i] + nums[j] < target and j gets incremented if nums[i] + nums[j] > target. 
We will construct a list of consiting of the original array elements and it's original index. Once we have our 
target we will return the original index of i and j in the new sorted array
'''
'''
nums = [3,4, 5, 6]
twosum
    - copy nums into 2d array (i.e. [[3, 0], [4, 1], [5, 2], [6, 3]])
    - sort the 2d nums array (i.e. [[3, 0], [4, 1], [5, 2], [6, 3]])
    - iterate through the sorted array stop when i >= j
    - compare nums2d[i][0] + nums2d[j][0] < target
        - increase i
    - > target
        - decrease j
    - = target
        return [min(nums2d[i][1], nums2d[j][1]), max(nums2d[i][1], nums2d[j][1])
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2d = [[x, i] for i, x in enumerate(nums) ]
        nums2d.sort()
        i = 0 
        j = len(nums) -1
        while i < j:
            res = nums2d[i][0] + nums2d[j][0] 
            if res < target:
                i+=1
            elif res > target:
                j-=1
            else:
                return [min(nums2d[i][1], nums2d[j][1]), max(nums2d[i][1], nums2d[j][1])]
        