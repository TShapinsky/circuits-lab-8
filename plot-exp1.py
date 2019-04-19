#!/usr/bin/env python3
# coding=utf-8
import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

plots = [{'Vb':.559, 'V2':[2.509,3.501,4.500]},{'Vb':1.085, 'V2':[2.503,3.499,4.500]}]

def read_file(file_name):
    f = open(file_name)
    c = csv.reader(f, delimiter=",")
    next(c)
    X = []
    Y = []
    for row in c:
        X.append(float(row[0]))
        Y.append(float(row[1]))
    return (np.array(X),np.array(Y))

for plot in plots:
    fig = plt.figure()
    ax = plt.subplot(111)
    for V2 in plot['V2'][::-1]:
        x,y = read_file('data/exp1_vb={:05.3f}_v2={:05.3f}.csv'.format(plot['Vb'],V2))
        plt.plot(x,y, '.', label='V2={:05.3f}'.format(V2))

    plt.title("Voltage Transfer Characteristic (Vb={:05.3f})".format(plot['Vb']))
    plt.legend()
    plt.xlabel("Vin (V)")
    plt.ylabel("Vout (V)")
    plt.savefig("exp1_Vb={:05.3f}.pdf".format(plot['Vb']))
    #plt.show()
