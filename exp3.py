#!/usr/bin/env python3
# coding=utf-8
import csv
import numpy as np
import matplotlib.pyplot as plt

"""
Configure your amplifier as a unity-gain follower by connecting the output to the inverting
input terminal. Measure V out as you sweep V in from one rail to the other. Fit a straight line
to the VTC that you obtain. Is the incremental gain close to unity? In your report, include
a plot showing V out versus V in along with the best-fit line. Repeat the sweep of V in while
measuring V out − V in directly. Include a plot of V out − V in versus V in in your report. This
plot represents the offset voltage of your amplifier. How does the offset voltage change as V in
changes?
"""

# First, the voltage-transfer characteristic

# Load data
Vin, Vout = [], []
with open("data/exp3_vb=1.085.csv") as f:
  c = csv.reader(f, delimiter=",")
  next(c) # Throw away the header
  for _ in range(2): # Throw away 2 bad data points
    next(c)
  for row in c:
    Vin += [float(row[0])]
    Vout += [float(row[1])]

# Remove the first bit of the data for linear fit.  Inefficient but works.
lin_fit_range = (1,4)
Vin_fit, Vout_fit = [], []
do_add = False
for (vin, vout) in zip(Vin, Vout):
  if vin > lin_fit_range[1]:
    do_add = False
  elif vin > lin_fit_range[0]:
    do_add = True
  if do_add:
    Vin_fit += [vin]
    Vout_fit += [vout]

# Do the linear fit
fit = np.polyfit(Vin_fit, Vout_fit, 1)
Vout_t = np.array(Vin_fit)*fit[0] + fit[1]

# Plot things
fig = plt.figure(figsize=(8,6))
ax = plt.subplot(111)
ax.plot(Vin, Vout, 'g.', markersize=4, label="Voltage transfer characteristic")
ax.plot(Vin_fit, Vout_t, 'r-', linewidth=1, label="Linear fit (slope = %g" % fit[0])

plt.title("Unity-gain follower voltage transfer characteristic")
plt.xlabel("Input voltage (V)")
plt.ylabel("Output voltage (V)")
plt.grid(True)
ax.legend()
plt.savefig("exp3_vtc.pdf")
plt.cla()


# Now let's do offset voltage!

# Load data
Vin, Vdiff = [], []
with open("data/exp3_direct_vb=1.085.csv") as f:
  c = csv.reader(f, delimiter=",")
  next(c) # Throw away the header
  for _ in range(2): # Throw away 2 bad data points
    next(c)
  for row in c:
    Vin += [float(row[0])]
    Vdiff += [float(row[1])]

# Plot things
ax.plot(Vin, Vdiff, 'g.', markersize=4, label="Offset voltage")

plt.title("Unity-gain follower offset voltage characteristic")
plt.xlabel("Input voltage (V)")
plt.ylabel("Offset voltage (V)")
plt.grid(True)
ax.legend()
plt.savefig("exp3_offset.pdf")
plt.cla()

