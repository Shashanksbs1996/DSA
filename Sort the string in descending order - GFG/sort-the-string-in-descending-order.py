#User function Template for python3
class Solution:
    def ReverseSort(self, x): 
       # code here
       x = sorted(x)
       s = x[::-1]
       return "".join(map(str,s))
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.ReverseSort(s))
# } Driver Code Ends