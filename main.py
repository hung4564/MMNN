from markov.M_M_1 import M_M_1
from markov.M_M_1_K import M_M_1_K
from markov.M_M_C import M_M_C
from markov.M_M_C_K import M_M_C_K
markov1 = M_M_1(0.4, 0.5)
markov1.diplay()
markov2 = M_M_1_K(0.4, 0.5, 3)
markov2.diplay()
markov3 = M_M_C(0.4, 0.5, 1)
markov3.diplay()
markov4 = M_M_C_K(0.4, 0.5, 1, 3)
markov4.diplay()
