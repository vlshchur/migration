#!/usr/bin/env python3

import sys
import os
import argparse
import numpy
from migrationIO import ReadJAFS
from math import log

parser = argparse.ArgumentParser(description='Implementation of TT-method (Schlebusch et al, Genetics 2017)')

parser.add_argument('jafs',
                    help='Joint allele frequency spectrum')
parser.add_argument('haplen',
                    help='Halotype length (total number of sites, both variable and non-variable)')

parser.add_argument('-y', nargs=1, type=float, default=1,
                    help='years per generation')
parser.add_argument('-mu', nargs=1, type=float, default=1.25e-8,
                    help='mutation rate (per basepair per generation)')

clargs = parser.parse_args()

if isinstance(clargs.y, list):
    clargs.y = clargs.y[0]
if isinstance(clargs.mu, list):
    clargs.mu = clargs.mu[0]

spectrum = ReadJAFS(clargs.jafs)
spectrum = spectrum[1:]
#Converting to paper notations
M = float(clargs.haplen)
spectrum = [512436, 179161, 481325, 279158, 255027, 181878, 281643]
m1 = spectrum[0]
m2 = spectrum[2]
m3 = spectrum[1]
m4 = spectrum[5]
m5 = spectrum[3]
m6 = spectrum[4]
m7 = spectrum[6]


print("m1=", m1)
print("m2=", m2)
print("m3=", m3)
print("m4=", m4)
print("m5=", m5)
print("m6=", m6)
print("m7=", m7)
print(m1/2+m3, "\t", (2*m6+m5)*(6*m7+m5)/8/m5)

T1 = (m1/2+m3-(2*m6+m5)*(6*m7+m5)/8/m5)/M
T2 = (m2/2+m4-(2*m7+m5)*(6*m6+m5)/8/m5)/M
print(T1)
print(T2)

a1 = 2*m5/(2*m6+m5)
a2 = 2*m5/(2*m7+m5)

theta = 3/M*(2*m6+m5)*(2*m7+m5)/(8*m5)/2
theta1 = -T1/log(a1)/2
theta2 = -T2/log(a2)/2

mu = clargs.mu
Ygen = clargs.y
T1y = T1/mu*Ygen
T2y = T2/mu*Ygen

N_A = theta/mu
N_1 = theta1/mu
N_2 = theta2/mu

print("Implementation of tt method (Schlebusch et al, Genetics 2017)")
print("T1 = ", T1y)
print("T2 = ", T2y)
print("N_A = ", N_A, "\tN_1 = ", N_1, "\tN_2 = ", N_2)

