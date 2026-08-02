class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = {}
        for words in strs:
            word = "".join(sorted(words))
            if word in lst:
                lst[word].append(words)
            else:
                lst[word] = [words]
        res = []
        for lists in lst.values():
            res.append(lists)

        return res