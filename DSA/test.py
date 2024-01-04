
from typing import List


class Solution:
    def powerup(self, N : int, K : int, energyArr : List[int]) -> int:
        # code here
        l=len(energyArr)
        c=l-2
        flag=False
        for i in range(l-2,-1,-1):
            req=0
            for j in range(i,l-1,1):
                
                req=req+energyArr[j+1]
            if(energyArr[i]==0):
                    req=req-K
            if(req<K):
                flag=True
                return i
                break
        # if flag==False:
        #     return -1



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = IntArray().Input()
        
        
        energyArr=IntArray().Input()
        
        obj = Solution()
        res = obj.powerup(N, K, energyArr)
        
        print(res)
        

# } Driver Code Ends