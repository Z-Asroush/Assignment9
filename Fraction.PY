class fraction:

    def __init__(self,s,m):
        self.soorat=s
        self.makhraj=m

    def sum(self,x):
        result=fraction(None,None)
        result.soorat=self.soorat*x.makhraj+x.soorat*self.makhraj
        result.makhraj=self.makhraj*x.makhraj
        return result

    def mul(self,x):
        result=fraction(None,None)
        result.soorat=self.soorat*x.soorat
        result.makhraj=self.makhraj*x.makhraj
        return result

    def sub(self,x):
        result=fraction(None,None)
        result.soorat=self.soorat*x.makhraj-x.soorat*self.makhraj
        result.makhraj=self.makhraj*x.makhraj
        return result

    def div(self,x):
        result=fraction(None,None)
        result.soorat=self.soorat*x.makhraj
        result.makhraj=self.makhraj*x.soorat
        return result

    def show(self):
        print(self.soorat,'/',self.makhraj)

A=fraction(3,5)
B=fraction(4,3)

A.show()
B.show()

c=A.mul(B)
c.show()

d=A.sub(B)
d.show()

e=A.sum(B)
e.show()

f=A.div(B)
f.show()