class M_M_1(object):
    def __init__(self, lamda, muy):
        self.lamda = float(lamda)
        self.muy = float(muy)

    def isVaild(self):
        return self.Rho() < 1

    def Rho(self):
        return self.lamda/self.muy

    def P0(self):
        """Xac xuat hang doi khong co khach hang"""
        if not self.isVaild():
            pass
        return 1 - self.Rho()

    def PN(self, n):
        """Xac xuat hang doi co n khach hang"""
        if not self.isVaild():
            pass
        if not self.isVaild():
            pass
        return self.P0()*self.Rho**n

    def L(self):
        """So luong phuc vu trung binh"""
        if not self.isVaild():
            pass
        return self.Rho()/(1-self.Rho())

    def Lq(self):
        """So luong khach khach doi trung binh"""
        if not self.isVaild():
            pass
        return self.L()*self.Rho()

    def W(self):
        """Thoi gian phuc vu trung binh"""
        if not self.isVaild():
            pass
        return self.L()/self.lamda

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
