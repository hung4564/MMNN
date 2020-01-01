import math


class M_M_C_K(object):
    def __init__(self, lamda, muy, C, K):
        self.lamda = float(lamda)
        self.muy = float(muy)
        self.C = int(C)
        self.K = int(K)

    def r(self):
        return self.lamda/self.muy

    def Rho(self):
        return self.r() / self.C

    def P0(self):
        sum = 0
        for i in range(0, self.C+1):
            sum += (self.r()**i)/math.factorial(i)

        temp = (self.r()**self.C)/math.factorial(self.C)
        if self.Rho() != 1:
            temp2 = 0
            for n in range(self.C + 1, self.K+1):
                temp2 += self.Rho()**(n - self.C)

            return 1/(sum + temp * temp2)
        elif self.Rho() == 1:
            return 1/(sum + temp * (self.K-self.C+1))

    def PN(self, n):
        if(n > self.C):
            return self.P0() * (self.Rho()**(n))/((self.C**(n-self.C)*math.factorial(self.C)))
        else:
            return self.P0() * (self.Rho()**(n))/math.factorial(n)

    def PK(self):
        return self.PN(self.K)

    def L(self):
        """So luong phuc vu trung binh"""
        return self.Lq() + self.r()

    def Lq(self):
        """So luong khach khach doi trung binh"""
        sum = 0
        for i in range(self.C, self.K+1):
            sum += (i-self.C)*self.PN(i)
        return sum

    def W(self):
        """Thoi gian phuc vu trung binh"""
        return self.Wq() + 1/self.muy

    def Wq(self):
        """Thoi gian doi trung binh"""
        return self.Lq()/self.lamda

    def diplay(self):
        print("He so co ich cua he thong: " + str(self.Rho()))
        print("So khach hang trung binh trong he thong: " + str(self.L()))
        print("So khach hang trung binh trong hang cho: " + str(self.Lq()))
        print("Thoi gian doi trung binh trong he thong: " + str(self.W()))
        print("Thoi gian doi trung binh trong hang cho: " + str(self.Wq()))
