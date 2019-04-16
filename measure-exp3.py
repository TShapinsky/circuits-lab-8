#!/usr/bin/env python2
# coding=utf-8
import smu
import numpy as np

s = smu.smu()

v = np.linspace(0, 5, 1000)

# vb = 0.559v -> ib = 1μA
# vb = 1.085 -> ib =  99.8μA
filename = "data/exp3_vb=1.085.csv"
measuring = "Vout"

f = open(filename, 'w')
f.write("Vout, {!s}\n".format(measuring))

s.set_voltage(1,0)
s.autorange(1)
s.set_voltage(2,3)
s.set_vrange(2, 0)

for val in v:
    s.set_voltage(1,val)
    s.autorange(1)
    s.set_current(2, 0)
    s.set_vrange(2, 0)
    f.write('{!s},{!s}\n'.format(val, s.get_voltage(2)))

s.set_current(1,0)
f.close()
