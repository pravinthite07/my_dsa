class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]

        for i in range (1,n):
            num = arr[i]
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, num*max_product)
            min_product = min(num, num*min_product)
            result = max(result, max_product)

        return result
if __name__ == "__main__":
    solution = Solution()

    arr1 = [2, 3, -2, 4]
    print("Output:", solution.maxProduct(arr1))  # Expected: 6 (Subarray: [2,3])

    arr2 = [-2, 3, -4]
    print("Output:", solution.maxProduct(arr2))  # Expected: 24 (Subarray: [3,-4])

    arr3 = [0, 2, -3, 4, -5]
    print("Output:", solution.maxProduct(arr3))  # Expected: 120 (Subarray: [2,-3,4,-5])

    arr4 = [-1, -2, -3, -4]
    print("Output:", solution.maxProduct(arr4))  # Expected: 24 (Subarray: [-1,-2,-3,-4])

    arr5 = [1, 0, -1, 2, 3, -5, -2]
    print("Output:", solution.maxProduct(arr5))  # Expected: 60 (Subarray: [2,3,-5,-2])