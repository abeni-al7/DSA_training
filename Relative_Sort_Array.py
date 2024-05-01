class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_dict = Counter(arr1)
        index = 0
        for num in arr2:
            count = count_dict[num]
            while index < len(arr1) and count > 0:
                arr1[index] = num
                index += 1
                count -= 1
            del count_dict[num]
        for x, y in sorted(count_dict.items()):
            count = y
            while index < len(arr1) and count > 0:
                arr1[index] = x
                index += 1
                count -= 1
        return arr1
