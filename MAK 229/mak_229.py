#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@Author: Baran Berk Bagci
"""

import math


class FluidSolver(object):

    def __init__(self):

        self.diameters = [4, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128]
        self.g = 9.81

        self.x = {'A': 2000, 'B': 4000, 'C': 3900, 'D': 4400, 'E': 4600}
        self.y = {'A': 1500, 'B': 2500, 'C': 500, 'D': 800, 'E': 2200}
        self.h = {'A': 126, 'B': 32, 'C': 41, 'D': 55, 'E': 66}
        self.Q = {'B': 0.024, 'C': 0.017, 'D': 0.029, 'E': 0.029}

        self.ReB = []
        self.ReC = []
        self.ReD = []
        self.ReE = []

        self.kB = []
        self.kC = []
        self.kD = []
        self.kE = []

        self.v = 1.3 * math.pow(10,-6)
        self.calculate_reynolds()

        self.fB = [0.02373, 0.023887, 0.024036, 0.024183, 0.024326, 0.024606, 0.024876, 0.025138, 0.025638, 0.026110, 0.026559, 0.0273980, 0.0281705, 0.0288895, 0.030201]
        self.fC = [0.02386, 0.024071, 0.024276, 0.0244762, 0.0246710, 0.02504713, 0.0254067, 0.025751, 0.026403, 0.027012, 0.027585, 0.028641, 0.0296026, 0.0304894, 0.0320913]
        self.fD = [0.02368, 0.023809, 0.023934, 0.02405714, 0.0241782, 0.0244148, 0.024644, 0.024867, 0.025296, 0.025705, 0.0260950, 0.0268279, 0.0275081, 0.0281448, 0.0293130]
        self.fE = [0.02368, 0.023809, 0.023934, 0.02405714, 0.0241782, 0.0244148, 0.024644, 0.024867, 0.025296, 0.025705, 0.0260950, 0.0268279, 0.0275081, 0.0281448, 0.0293130]

        self.calculate_distance()

        self.calculate_loss()

    def calculate_reynolds(self):

        for D in self.diameters:
            ReB = ((4*self.Q['B'])/(math.pi*(D*0.01)))/self.v
            ReC = ((4*self.Q['C'])/(math.pi*(D*0.01)))/self.v
            ReD = ((4*self.Q['D'])/(math.pi*(D*0.01)))/self.v
            ReE = ((4*self.Q['E'])/(math.pi*(D*0.01)))/self.v

            self.ReB.append(float("{0:.5f}".format(ReB)))
            self.ReC.append(float("{0:.5f}".format(ReC)))
            self.ReD.append(float("{0:.5f}".format(ReD)))
            self.ReE.append(float("{0:.5f}".format(ReE)))
        print("Re B: ",self.ReB)
        print("Re C: ",self.ReC)
        print("Re D: ",self.ReD)
        print("Re E: ",self.ReE)

    def calculate_distance(self):
        self.LAB = (((self.x['A'] - self.x['B'])**2) + ((self.y['A'] - self.y['B'])**2)) ** 0.5
        self.LAE = (((self.x['A'] - self.x['E'])**2) + ((self.y['A'] - self.y['E'])**2)) ** 0.5
        self.LAD = (((self.x['A'] - self.x['D'])**2) + ((self.y['A'] - self.y['D'])**2)) ** 0.5
        self.LAC = (((self.x['A'] - self.x['C'])**2) + ((self.y['A'] - self.y['C'])**2)) ** 0.5
        self.LED = (((self.x['E'] - self.x['D'])**2) + ((self.y['E'] - self.y['D'])**2)) ** 0.5
        self.LEC = (((self.x['E'] - self.x['C'])**2) + ((self.y['E'] - self.y['C'])**2)) ** 0.5

        print("LAB: ",self.LAB)
        print("LAE: ",self.LAE)
        print("LAD: ",self.LAD)
        print("LAC: ",self.LAC)
        print("LED: ", self.LED)
        print("LEC: ",self.LEC)

    def calculate_loss(self):
        
        """ First Topholgy"""
        # for i in range(len(self.diameters)):
            
        #     kB = ((94*2*self.g)/((4*self.Q['B']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fB[i] * 2330.0679/(self.diameters[i] * 0.01)))
        #     kE = ((60*2*self.g)/((4*self.Q['E']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fE[i] * 2752.5824/(self.diameters[i] * 0.01)))
        #     kD = ((71*2*self.g)/((4*self.Q['D']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fD[i] * 2571/(self.diameters[i] * 0.01)))
        #     kC = ((85*2*self.g)/((4*self.Q['C']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fC[i] * 2232.0910/(self.diameters[i] * 0.01)))
        #     self.kB.append(kB)
        #     self.kE.append(kE)
        #     self.kD.append(kD)
        #     self.kC.append(kC)
        
        # print("\nFirst Topology\n")
        # print("Kb: ", self.kB)
        # print("Ke: ", self.kE)
        # print("Kd: ", self.kD)
        # print("Kc: ", self.kC)

        # print("Db: ", self.diameters[self.kB.index(936.0514565063381)])
        # print("De: ",self.diameters[self.kE.index(145.8430272117331)])
        # print("Dd: ",self.diameters[self.kD.index(277.2933233824174)])
        # print("Dc: ",self.diameters[self.kC.index(279.2170538077087)])

        # print("\n\n\n")
        
        """End of First Topology"""

        """Second Topolgy"""
        # for i in range(len(self.diameters)):
            
        #     kB = ((94*2*self.g)/((4*self.Q['B']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fB[i] * 2330.0679/(self.diameters[i] * 0.01)))
        #     kE = ((60*2*self.g)/((4*self.Q['E']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fE[i] * 2752.5824/(self.diameters[i] * 0.01)))
        #     kD = ((11*2*self.g)/((4*self.Q['D']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fD[i] * 1425.221/(self.diameters[i] * 0.01)))
        #     kC = ((25*2*self.g)/((4*self.Q['C']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fC[i] * 1863.47763/(self.diameters[i] * 0.01)))
        #     self.kB.append(kB)
        #     self.kE.append(kE)
        #     self.kD.append(kD)
        #     self.kC.append(kC)
        
        # print("\nSecond Topology\n")

        # print("Kb: ", self.kB)
        # print("Ke: ", self.kE)
        # print("Kd: ", self.kD)
        # print("Kc: ", self.kC)

        # print("Db: ", self.diameters[self.kB.index(936.0514565063381)])
        # print("De: ",self.diameters[self.kE.index(145.8430272117331)])
        # print("Dd: ",self.diameters[self.kD.index(77.66108429475696)])
        # print("Dc: ",self.diameters[self.kC.index(394.40394729473303)])

        # print("\n\n\n")

        """End of second tophology"""

        """Third Topology"""
        for i in range(len(self.diameters)):
            
            kB = ((94*2*self.g)/((4*self.Q['B']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fB[i] * 2330.0679/(self.diameters[i] * 0.01)))
            kE = ((60*2*self.g)/((4*self.Q['E']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fE[i] * 2752.5824/(self.diameters[i] * 0.01)))
            kD = ((11*2*self.g)/((4*self.Q['D']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fD[i] * 1425.221/(self.diameters[i] * 0.01)))
            kC = ((85*2*self.g)/((4*self.Q['C']/((math.pi * ((self.diameters[i] * 0.01)**2))))**2) - (self.fC[i] * 2232.0910/(self.diameters[i] * 0.01)))
            self.kB.append(kB)
            self.kE.append(kE)
            self.kD.append(kD)
            self.kC.append(kC)

        print("\nThird Topology\n")

        print("Kb: ", self.kB)
        print("Ke: ", self.kE)
        print("Kd: ", self.kD)
        print("Kc: ", self.kC)

        print("Db: ", self.diameters[self.kB.index(936.0514565063381)])
        print("De: ",self.diameters[self.kE.index(145.8430272117331)])
        print("Dd: ",self.diameters[self.kD.index(77.66108429475696)])
        print("Dc: ",self.diameters[self.kC.index(279.2170538077087)])

        print("\n\n\n")

        """End of third topholgy"""

if __name__ == "__main__":
    fluid = FluidSolver()