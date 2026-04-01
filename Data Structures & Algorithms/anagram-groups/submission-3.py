class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       #we can use a dict with the key being an array of 
       #each letter in the alpa and value being words 

       words = defaultdict(list)

       for word in strs:
            key = [0] * 26
            for char in word:
                key[ord(char) - ord('a')] += 1
            words[tuple(key)].append(word)
       return list(words.values())




        
       
        
        