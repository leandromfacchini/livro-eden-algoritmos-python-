# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# Parâmetros clássicos
sigma = 10
rho = 28
beta = 8/3

dt = 0.01
steps = 10000

xs = np.zeros(steps)
ys = np.zeros(steps)
zs = np.zeros(steps)

xs[0], ys[0], zs[0] = (0., 1., 1.05)

for i in range(steps - 1):
    xs[i+1] = xs[i] + sigma*(ys[i] - xs[i]) * dt
    ys[i+1] = ys[i] + (xs[i]*(rho - zs[i]) - ys[i]) * dt
    zs[i+1] = zs[i] + (xs[i]*ys[i] - beta*zs[i]) * dt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(xs, ys, zs)
plt.show()

# %%
