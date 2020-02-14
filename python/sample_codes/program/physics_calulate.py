# -*- coding: cp936 -*-

#this module can work out some physical math problem
import math
from math import *
h=6.55e-34#     unit Js, Plank's constant
k_B=1.38065e-23#unit J/K , Boltzmann constant
c=3e8#          unit m/s, speed of light in vaccum
b=2897768.5#    unit  nm·K, constant in Wien's displacement law, Lambda(max)*T=b
e=1.6e-19#      the charge of proton
G=6.67e-11     #Gravitational constant
m_e=9.11e-31   # mass of electron
m_p=1.67e-27   # mass of proton
m_alpha=6.64465675e-27 # unit kg, mass of alpha-particle: helium nucleus

def main1():#gravity force and coulomb force
    k=8.99e9
    e=1.6e-19#the charge of proton
    r=5.29e-11#
    G=6.67e-11#Gravitational constant
    m_e=9.11e-31# mass of electron
    m_p=1.67e-27#
    f1=k*e*e/(r*r)#the formula of ...
    f2=G*m_e*m_p/(r*r)#the formula of gravity
def main2():
    r=6.9e-15#
    e=1.6e-19
    E0=8.85e-12
    k=1.0/(4*pi*E0)
    U=k*q/r
    print 'U=',U
def main3():#re xue P55,5
    R,NA=8.20574e-2,2.6868e25
    print p*NA/(R*t)
    print 32.0*p*NA/(R*t)
    
main5()



"""
希腊字母读法 
Αα：阿尔法 Alpha 
Ββ：贝塔 Beta 
Γγ：伽玛 Gamma 
Δδ：德尔塔 Delte 
Εε：艾普西龙 Epsilon 
ζ ：捷塔 Zeta 
Ζη：依塔 Eta 
Θθ：西塔 Theta 
Ιι：艾欧塔 Iota 
Κκ：喀帕 Kappa 
∧λ：拉姆达 Lambda 
Μμ：缪 Mu 
Νν：拗 Nu 
Ξξ：克西 Xi 
Οο：欧麦克轮 Omicron 
∏π：派 Pi 
Ρρ：柔 Rho 
∑σ：西格玛 Sigma 
Ττ：套 Tau 
Υυ：宇普西龙 Upsilon 
Φφ：fai Phi 
Χχ：器 Chi 
Ψψ：普赛 Psi 
Ωω：欧米伽 Omega
"""
