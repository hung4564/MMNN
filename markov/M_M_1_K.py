class M_M_1_K(object):
    def __init__(self, lamda, muy, k):
        self.lamda = float(lamda)
        self.muy = float(muy)
        self.K = int(k)

    def Rho(self):
        return self.lamda/self.muy

    def P0(self):
        """Xac xuat hang doi khong co khach hang"""
        if self.Rho() != 1:
            return (1 - self.Rho())/(1 - self.Rho()**(self.K + 1))
        elif self.Rho() == 1:
            return 1/(self.K + 1)

    def PN(self, n):
        """Xac xuat hang doi co n khach hang"""
        if self.Rho() != 1:
            return (self.Rho()**n)*(1 - self.Rho())/(1 - self.Rho()**(self.K + 1))
        elif self.Rho() == 1:
            return 1/(self.K + 1)

    def PK(self):
        """Xac xuat hang doi co day"""
        return self.PN(self.K)

    def L(self):
        """So luong phuc vu trung binh"""
        if self.Rho() != 1:
            temp1 = 1 + (self.K * (self.Rho()**(self.K + 1))) - \
                (self.K + 1)*(self.Rho()**self.K)
            temp2 = (1 - self.Rho())*(1 - self.Rho()**(self.K + 1))
            return self.Rho()*temp1/temp2
        elif self.Rho() == 1:
            return self.K/2

    def Lq(self):
        """So luong khach khach doi trung binh"""
        if self.Rho() != 1:
            temp1 = self.Rho()*(1 - self.Rho()**(self.K))
            temp2 = 1 - self.Rho()**(self.K + 1)
            return self.L() - (temp1/temp2)
        elif self.Rho() == 1:
            return self.K*(self.K - 1) / (2*(self.K + 1))

    def W(self):
        """Thoi gian phuc vu trung binh"""
        return self.L()/(self.lamda*(1 - self.PK()))

    def Wq(self):
        """Thoi gian doi trung binh"""
        return self.W()-1/self.muy

    def diplay(self):
        print("He so co ich cua he thong: " + str(self.Rho()))
        print("So khach hang trung binh trong he thong: " + str(self.L()))
        print("So khach hang trung binh trong hang cho: " + str(self.Lq()))
        print("Thoi gian doi trung binh trong he thong: " + str(self.W()))
        print("Thoi gian doi trung binh trong hang cho: " + str(self.Wq()))
