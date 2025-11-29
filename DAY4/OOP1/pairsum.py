class PairFinding:

    def __init__(self,sum,n,Value):
      self.sum=sum
      self.n=n
      self.Values=Values
    def findPair(self):
       n=len(self.Values)
       Pairsfound=[]
       for i in range(n):
           for j in range(i+1,n):
               if self.Values[i]+self.Values[j]==self.sum:
                  Pairsfound.append((self.Values[i],self.Values[j]))
       return Pairsfound
    def displaypairs(self):
       pairs=self.findpairs()
       for a,b in pairs:
           print(f"({a},{b})")


# MAIN()

sum=30
n=8
Values=[14,-15,9,16,15,25,45,12,8]
pairResult=PairFinding(sum,n,Values)
pairResult.displaypairs()