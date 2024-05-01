class Solution:
    def smallestNumber(self, num: int) -> int:
        my_list = sorted(str(abs(num)))
        if num <= 0:
            return -int(''.join(my_list[::-1]))
        i = 0
        while my_list[i] == '0':
            i += 1
        my_list[i], my_list[0] = my_list[0], my_list[i]
        return int(''.join(my_list))
