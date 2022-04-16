#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Baran Berk Bağcı
"""

import math
import numpy as np
import matplotlib.pyplot as plt

theta_max = 45 * math.pi/180

t = 51.5276 * math.sin(theta_max)/9.81

t_total = np.arange(0, t*2, 0.1) 

y = []
for i in range(len(t_total)):

    y.append(((51.5276 * math.sin(theta_max) * t_total[i]) - (0.5*9.81*t_total[i]**2) + 1.5))

plt.figure(figsize = (12, 8))
plt.plot(t_total, y, 'bo--', label='trajectory')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Trajectory')
plt.grid()
plt.legend(loc='lower right')
plt.show()