#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Author: Baran Berk Bağcı
"""

import numpy as np
import matplotlib.pyplot as plt


# Part d Fx and Vx calculation and plotting
class Arrow(object):
    def __init__(self):
        self.ax = lambda t, s: -3.6661*t
        self.h = 0.1
        self.t = np.arange(0, 7, self.h)
        self.v0 = 42.2089
        self.v = np.zeros(len(self.t))
        self.v[0] = self.v0
        self.backward_EULER()

    def backward_EULER(self):
        for i in range(0, len(self.t) - 1):
            self.v[i + 1] = self.v[i] + self.h*self.ax(self.t[i], self.v[i])
        plt.figure(figsize = (12, 8))
        plt.plot(self.t, self.v, 'bo--', label='Approximate')
        plt.plot(self.t, self.v0-3.6661*self.t, 'g', label='Exact')
        plt.title('Approximate and Exact Solution \
        for Simple ODE')
        plt.xlabel('t')
        plt.ylabel('f(t)')
        plt.grid()
        plt.legend(loc='lower right')
        plt.show()

if __name__ == "__main__":
    arrow = Arrow()