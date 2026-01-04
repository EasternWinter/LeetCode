class Solution:
    '''def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr[:]

        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result'''

    def countSmaller(self, nums: List[int]) -> List[int]:
        '''l = len(nums)
        counts = [0] * l
        n = self.mergeSort(nums)
        if n == nums:
            return counts
        for i in range(l-1):
            for j in range(i, l):
                if nums[j] < nums[i]:
                    counts[i] += 1
        return counts'''
        n = len(nums)
        counts = [0] * n
        
        #Pair each number with its index
        enum = list(enumerate(nums))
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            merged = []
            i = j = 0
            
            while i < len(left) and j < len(right):
                #If left value is greater, right is smaller
                if left[i][1] > right[j][1]:
                    counts[left[i][0]] += len(right) - j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        
        merge_sort(enum)
        return counts