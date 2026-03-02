#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
# Parâmetros clássicos
a = 0.2
b = 0.2
c = 5.7

dt = 0.01
steps = 10000

xs = np.zeros(steps)
ys = np.zeros(steps)
zs = np.zeros(steps)

xs[0], ys[0], zs[0] = (0., 1., 1.)

for i in range(steps - 1):
    xs[i+1] = xs[i] + (-ys[i] - zs[i]) * dt
    ys[i+1] = ys[i] + (xs[i] + a*ys[i]) * dt
    zs[i+1] = zs[i] + (b + zs[i]*(xs[i] - c)) * dt


#%%
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(xs, ys, zs)
plt.show()
# %%
