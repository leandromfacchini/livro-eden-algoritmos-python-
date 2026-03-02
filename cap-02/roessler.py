# %%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as fig
from mpl_toolkits import mplot3d
# %%

# condicao inicial de X
X0 = 0

# condicao inicial de Y
Y0 = 1

# condicao incial de Z
Z0 = 0

# Parametros do sistema
a = 0.1
b = 0.1
c = 18

# grade de tempos t
t = np.linspace(0, 160, 5000)

# sistema de eq. diferenciais de Rossler


def deriv(s, t, a, b, c):
    X, Y, Z = s
    dXdt = -Y - Z
    dYdt = X + a*Y
    dZdt = b+(X-c)*Z
    return dXdt, dYdt, dZdt


# condicoes iniciais no Vetor
s0 = X0, Y0, Z0

# integracao do sistema
res = odeint(deriv, s0, t, args=(a, b, c))
X, Y, Z = res.T


# %%

# plot dados separados X,Y,Z
ax = fig.subplot(311, facecolor='#dddddd', axisbelow=True)
ax.plot(t, X, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('X')

ax = fig.subplot(312, facecolor='#dddddd', axisbelow=True)
ax.plot(t, Y, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('Y')

ax = fig.subplot(313, facecolor='#dddddd', axisbelow=True)
ax.plot(t, Z, 'k')
ax.set_xlabel('Tempo')
ax.set_ylabel('Z')

fig.figure()
ax2 = fig.axes(projection='3d')
ax2.plot3D(X, Y, Z, '-k')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

# %%
