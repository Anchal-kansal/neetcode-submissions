class Solution:

    def encode(self, strs: List[str]) -> str:
        s=''
        for str in strs:
            s=s+f"{len(str)}#{str}"
        return s
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i < len(s):
            j=s.index('#',i)
            length=int(s[i:j])
            result.append(s[j+1:j+1+length])
            i=j+1+length
        return result