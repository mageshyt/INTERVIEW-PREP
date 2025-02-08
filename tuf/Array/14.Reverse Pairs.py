def reversePairs(nums):
    def merge_sort(lo, hi):
        # Base case: single element has no reverse pair
        if lo >= hi:
            return 0
        
        mid = (lo + hi) // 2
        count = merge_sort(lo, mid) + merge_sort(mid + 1, hi)
        
        # Count reverse pairs: for each element in the left subarray,
        # find how many elements in the right subarray satisfy the condition.
        j = mid + 1
        for i in range(lo, mid + 1):
            while j <= hi and nums[i] > 2 * nums[j]:
                j += 1
            count += j - (mid + 1)
        
        # Merge the two sorted halves
        temp = []
        left, right = lo, mid + 1
        while left <= mid and right <= hi:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        # Append any remaining elements
        while left <= mid:
            temp.append(nums[left])
            left += 1
        while right <= hi:
            temp.append(nums[right])
            right += 1
        
        # Copy the merged list back into nums
        nums[lo:hi + 1] = temp
        
        return count

    return merge_sort(0, len(nums) - 1)

# Example usage:
if __name__ == "__main__":
    # Example 1:
    nums1 = [6, 4, 4, 2, 2]
    print("Number of reverse pairs in {}: {}".format(nums1, reversePairs(nums1)))  # Expected output: 3

    # Example 2:
    nums2 = [5, 4, 4, 3, 3]
    print("Number of reverse pairs in {}: {}".format(nums2, reversePairs(nums2)))  # Expected output: 0
