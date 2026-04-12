class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        for num in nums:
            if num not in seq:
                seq[num] = 1

        max_sequence = 0

        for num in seq.keys():
            if seq[num] == 0:
                continue

            seq[num] = 0
            sequence = 1
            nextt = num + 1
            while nextt in seq:
                sequence += 1
                seq[nextt] = 0
                nextt += 1
            prev = num -1
            while prev in seq:
                sequence +=1
                seq[prev] = 0
                prev -= 1
            
            if sequence > max_sequence:
                max_sequence = sequence

        return max_sequence
