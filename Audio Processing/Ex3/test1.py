import numpy as np
import matplotlib.pyplot as plt

a = 5

fs = 10

t_attack1 = np.arange(0, a, 1/fs)
t_attack2 = [(x/fs) for x in range(a*fs) ]
print (t_attack1)
print (t_attack2)