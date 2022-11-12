#그룹 애너그램
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #정렬해서 딕셔너리에 추가함
        anagrams = collections.defaultdict(list)

        for word in strs:
            # join에 대한 설명:
            # b = 'zbdaf'
            # ''.join(sorted(b))
            # 'abdfz'
            # sort() 메소드와는 다름. sort()메소드는 리스트 자체를 제자리 정렬함.
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())