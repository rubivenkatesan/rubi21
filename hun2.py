#rubi
class LargestNumc:
    def __init__(self):
        self.n=int(input())
        self.narr=input()

    def Findc(self):
        narr=self.narr.split(" ")
        narr=[int(i) for i in narr]
        narr.sort()
        narr=[str(i) for i in narr]
        narr="".join(narr)
        narr=narr[::-1]
        narr=int(narr)
        print(narr)

ln=LargestNumc()
ln.Findc()
