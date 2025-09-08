class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n):
        # Track if any swap happens
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
        # If no swaps occurred, the array is already sorted
            if not swapped:
                break
        return arr