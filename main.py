from markov.M_M_1 import M_M_1
from markov.M_M_1_K import M_M_1_K
from markov.M_M_C import M_M_C
from markov.M_M_C_K import M_M_C_K

# markov1 = M_M_1(8, 10)
# markov1.diplay()
# markov2 = M_M_1_K(8, 10, 3)
# markov2.diplay()
# markov3 = M_M_C(8, 10, 1)
# markov3.diplay()
# markov4 = M_M_C_K(8, 10, 1, 3)
# markov4.diplay()

# markov5 = M_M_C(6, 8, 2)
# markov5.diplay()
# r = markov5.L()*8*30*200000.0 - markov5.C*7000000.0
# print("Loi nhuan hang thang la: "+str(r))
markov5 = M_M_1_K(6, 8, 4)
markov5.diplay()
r = markov5.L()*8*30*200000.0 - (markov5.K-4)*2000000 - 7000000
print("Loi nhuan hang thang la: "+str(r))
