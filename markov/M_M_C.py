import math


class M_M_C(object):
    def __init__(self, lamda, muy, C):
        self.lamda = float(lamda)
        self.muy = float(muy)
        self.C = int(C)

    def r(self):
        return self.lamda/self.muy

    def Rho(self):
        return self.r()/self.C

    def isVaild(self):
        return self.Rho() < 1

    def P0(self):
        """Xac xuat hang doi khong co khach hang"""
        if not self.isVaild():
            pass
        sum = 0
        temp = ((self.r()**self.C)*self.C) / \
            (math.factorial(self.C)*(self.C - self.r()))
        for i in range(0, self.C):
            sum += ((self.lamda/self.muy)**i)/(math.factorial(i))
        return 1/(sum + temp)

    def PN(self, n):
        """Xac xuat hang doi co n khach hang"""
        if not self.isVaild():
            pass
        if n < self.C:
            return self.P0()*(self.r()**n)/math.factorial(n)
        else:
            return self.P0()*(self.r()**n)/(math.factorial(self.C)*self.C**(n-self.C))

    def L(self):
        """So luong phuc vu trung binh"""
        if not self.isVaild():
            pass
        return self.Lq() + self.r()

    def Lq(self):
        """So luong khach khach doi trung binh"""
        if not self.isVaild():
            pass
        temp = ((self.r()**self.C)*self.Rho()) / \
            (math.factorial(self.C)*((1 - self.Rho())**2))
        return temp*self.P0()

    def W(self):
        """Thoi gian phuc vu trung binh"""
        if not self.isVaild():
            pass
        return self.Wq() + 1/self.muy

    def Wq(self):
        """Thoi gian doi trung binh"""
        if not self.isVaild():
            pass
        return self.Lq()/self.lamda

    def diplay(self):
        if self.isVaild():
            print("He so co ich cua he thong: " + str(self.Rho()))
            print("So khach hang trung binh trong he thong: " + str(self.L()))
            print("So khach hang trung binh trong hang cho: " + str(self.Lq()))
            print("Thoi gian doi trung binh trong he thong: " + str(self.W()))
            print("Thoi gian doi trung binh trong hang cho: " + str(self.Wq()))
        else:
            print("He thong khong on dinh")
