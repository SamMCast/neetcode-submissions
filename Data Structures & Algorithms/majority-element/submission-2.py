class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        bits = [0 for i in range(32)]

        maxbitlen = 0
        for num in nums:
            bitLen = num.bit_length()
            for i in range(32):
                bit = (num >> i) & 1
                if bit == 1:
                    bits[31-i] +=1

        #check if the majority element is negative or positive
    
        for i in range(32):
            if bits[i] > len(nums)//2:
                bits[i] = '1'
            else:
                bits[i] = '0'

        binary_str = "".join(bits)
        res = int(binary_str,2)
        if bits[0] == '1':
            res -= (1 <<32)

        return res
        