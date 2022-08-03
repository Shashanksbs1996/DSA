class Solution:
    def removeDuplicates(self, s: str) -> str:
        st=[]
        for el in s:
            if not st or st[-1] !=el:
                st.append(el)
            else:
                st.pop()
        return "".join(st)
        