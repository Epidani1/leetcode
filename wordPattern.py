class Solution:
    def wordPattern(self, pattern, st):
        s = pattern
        t = st.split()

        for ss, pp in s,t:
            
        
sn = Solution()
print(sn.wordPattern("abbbaa", "dog cat dog dog dog cat"))