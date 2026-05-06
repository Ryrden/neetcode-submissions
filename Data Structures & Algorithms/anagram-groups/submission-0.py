class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hash = defaultdict(list)
        
        for word in strs:
            freq = [0] * 26

            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            
            word_hash[tuple(freq)].append(word)
    
        return [ group for group in word_hash.values() ]