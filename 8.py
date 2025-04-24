import numpy as np
import matplotlib.pyplot as plt


class pendulum:
    def __init__(self, damping, amplitude, frequency):
        self.d = damping
        self.a = amplitude
        self.omega = frequency

    def __call__(self, y, t):
        velocity = y[1]  # первое дифференциальное уравнение
        acceleration = -self.d * y[1] - np.sin(y[0]) + self.a * np.cos(
            self.omega * t)  # второе дифференциальное уравнение
        return np.array([velocity, acceleration])


class rk:
    def __init__(self, f):
        self.f = f

    def setfunc(self, f):
        self.f = f

    def setparams(self, u0, t0, tmax, h):
        self.u0 = u0
        self.t0 = t0
        self.tmax = tmax
        self.h = h

    def rk4(self, u, t):
        k1 = self.f(u, t)
        k2 = self.f(u + self.h * k1 / 2, t + self.h / 2)
        k3 = self.f(u + self.h * k2 / 2, t + self.h / 2)
        k4 = self.f(u + self.h * k3, t + self.h)
        return u + (k1 + 2 * (k2 + k3) + k4) * self.h / 6

    def solve(self):
        y = self.u0
        solution = np.empty((0, 2))
        time = np.arange(self.t0, self.tmax, self.h)
        for t in time:
            y = self.rk4(y, t)
            solution = np.append(solution, [y], axis=0)
        return solution, time


fig, ax = plt.subplots(2)
f1 = pendulum(damping=0.01, amplitude=0.05, frequency=1.2)
u0 = np.array([3.0, 0.0])  # начальные условия
d = rk(f1)
d.setparams(u0, 0.0, 100, 0.1)
y, t = d.solve()
ax[0].plot(t, y[:, 0], label='x')
ax[0].plot(t, y[:, 1], label='dx/dt')
ax[0].legend()
ax[1].plot(y[:, 1], y[:, 0], label='фазовый портрет')
ax[1].legend()
# меняем параметры маятника
f1 = pendulum(damping=0, amplitude=0, frequency=0)
d.setfunc(f1)
y, t = d.solve()
ax[0].plot(t, y[:, 0], label='x_0')
ax[0].plot(t, y[:, 1], label='dx/dt_0')
ax[0].legend()
ax[1].plot(y[:, 1], y[:, 0], label='фазовый портрет_0')
ax[1].legend()

plt.show()
