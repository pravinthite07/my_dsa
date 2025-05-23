class Solution:
    def productExceptSelf(self,arr):
        n = len(arr)
        res = [1]*n

        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= arr[i]

        right_product = 1
        for i in range(n-1,-1,-1):
            res[i] *= right_product
            right_product *= arr[i]

        return res

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    print("Input:", nums1)
    print("Output:", solution.productExceptSelf(nums1))  # Expected: [120, 60, 40, 30, 24]

    # Test Case 2 (with zero)
    nums2 = [1, 0, 3, 4]
    print("\nInput:", nums2)
    print("Output:", solution.productExceptSelf(nums2))  # Expected: [0, 12, 0, 0]

    # Test Case 3 (all same numbers)
    nums3 = [2, 2, 2, 2]
    print("\nInput:", nums3)
    print("Output:", solution.productExceptSelf(nums3))  # Expected: [8, 8, 8, 8]

    # Test Case 4 (single element)
    nums4 = [10]
    print("\nInput:", nums4)
    print("Output:", solution.productExceptSelf(nums4))  # Expected: [1]    
