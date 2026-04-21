'''
Another approach is the use the prefix and suffix strategy. We need to compute 
the product of all elements to left of a particular index and to the right 
of said index. The product of those two (i.e. left product and right product)
will produce the product of all elements except the element found in that index. 
To accomplish this will use an array to store the product of all elements to 
the left of the index you're evaluating. It contain the product of leftward elements
minus the current index. At index 0, it will be 1, and then at index 1 it will 
be product of the element at index 0 and leftward product of all elements
at index 0 (i.e. 1). Index 2 will follow the same, the product of the element at
index 1 and leftward product at index 1. This will continue till index n-1. 
We will apply this approach for the right too. At index n-1 it will be rightward product
of n and n which in both cases we will say is 1. Then at index n-2, it will the
product of the element at index n-1 and the rightward product at index n-1. For computing
the rightward product, we can use a rightward product array and the final output
would be at index i the product leftward product array at index i and rightward product
array at the same index. 
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) ==2:
            nums[0], nums[1] =nums[1], nums [0]
            return nums
        output = [1 for x in range (len(nums))]

        left = [1 for x in range (len(nums))]
        right = [1 for x in range (len(nums))]

        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] * nums[j+1]

        return [right[i] * left[i] for i in range(len(nums))]
        