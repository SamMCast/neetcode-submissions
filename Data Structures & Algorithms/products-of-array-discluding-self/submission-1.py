'''
The solution to the this is easy to compute assuming that there are no 0s present
in the input array. If there are no zeros, then I can compute the product
of the entire array and store that in a variable called product. Then in the output
array, I take the product and divide by the value in that cell to get the 
product of all the elements except that cell. This is the best case scenario. 
If there is 0 zero, the output array will contain the product of all input array
elements except for the cell containing 0, and every other cell will be 0. 
If there are multiple 0s then the output array will contain all 0s. 
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        for num in nums:
            if num != 0:
                product = product * num
            else:
                zeros+=1
        
        if zeros > 1:
            return [0]* len(nums)
        
        elif zeros == 1:
            return [product if x == 0 else 0 for x in nums]
        else:
            return [product//x for x in nums]