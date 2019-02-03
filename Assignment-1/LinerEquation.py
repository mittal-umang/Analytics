class LinerEquation:
    def __init__(self, a=1, b=1, c=1, d=1, e=1, f=1):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        if self.getA() * self.getD() - self.getB() * self.getC() != 0:
            return True
        else:
            return False

    def getX(self):
        return (self.getE() * self.getD() - self.getB() * self.getF()) / \
               (self.getA() * self.getD() - self.getB() * self.getC())

    def getY(self):
        return (self.getA() * self.getF() - self.getE() * self.getC()) / \
               (self.getA() * self.getD() - self.getB() * self.getC())


def main():
    a, b, c, d, e, f = eval(input("Enter a,b,c,d,e,f : "))

    linerEquation = LinerEquation(a, b, c, d, e, f)
    if not linerEquation.isSolvable():
        print("The equation has no solution")
    else:
        print("The equation is solvable.")
        print("x = ", linerEquation.getX())
        print("y = ", linerEquation.getY())


if __name__ == "__main__":
    main()
