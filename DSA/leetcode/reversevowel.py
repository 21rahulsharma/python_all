class Solution:
    def reverseVowels(self, s: str) -> str:
        l=[]
        s2=""
        for i in s:
            if i=='A' or i=='E 'or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                l.append(i)
        for i in s:
            if i=='A' or i=='E 'or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                s2=s2+l.pop()
            else:
                s2=s2+i
        return s2
if __name__=='__main__':
    s=Solution()
    r=s.reverseVowels("oe")
    print(r)