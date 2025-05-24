class Solution:
    def maxSubArraySum(self, arr):  # ✅ Now it's inside a class
        max_sum = float('-inf')
        current_sum = 0
        
        for num in arr:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            
            if current_sum < 0:
                current_sum = 0
                
        return max_sum

# ✅ Test Cases
if __name__ == "__main__":
    solution = Solution()  # ✅ Create an instance of the class

    arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Output:", solution.maxSubArraySum(arr1))  # ✅ Correct way to call it
