import random
import matplotlib.pyplot as plt
import numpy as np

inside = 0
outside = 0

trial = []
results = []

for i in range(1,10000+1):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if y < (-x**2+1)**0.5:
        inside += 1
    elif y > (-x**2+1)**0.5:
        outside += 1
    else:
        on_arc += 1
    p = 4*inside/(inside + outside + 0.00000001)
    trial.append(i)
    results.append(p)
    
plt.axhline(np.pi)
plt.plot(trial,results,"red")
plt.show()
