class Solution:
    def sortSentence(self, s: str) -> str:
        s= s.split()
        l =[""]*len(s)
        for i in s:
            index = int(i[-1])-1
            l[index] = i[:-1]
        return " ".join(l)
