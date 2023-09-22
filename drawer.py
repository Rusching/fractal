class Solution():
    def equalFrequency(self, word: str) -> bool:
            from collections import defaultdict
            occurance_map = defaultdict(int)
            for each in word:
                occurance_map[each] += 1
            values = list(occurance_map.values())
            flag = False
            for i in range(len(values)):
                values[i] -= 1
                distin = set()
                for each in values:
                    if each != 0: distin.add(each)
                if len(distin) == 1: flag = True
                values[i] += 1
            return flag
ss = Solution()
print(ss.equalFrequency("aaccc"))
print(ss.equalFrequency("abac"))
print(ss.equalFrequency("bac"))
print(ss.equalFrequency("aazz"))