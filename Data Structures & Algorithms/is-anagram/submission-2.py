class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s={}
        count_t={}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i not in count_s:
                    count_s[i]=0
                count_s[i]=count_s[i]+1
            for j in t:
                if j not in count_t:
                    count_t[j]=0
                count_t[j]=count_t[j]+1

            return count_s == count_t
        #     return sorted(s) == sorted(t)