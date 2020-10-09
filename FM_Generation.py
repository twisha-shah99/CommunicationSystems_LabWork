#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Roll No: 191061902
# Date: October 8,2020
# Subject: PCS
# T.Y. B.tech Electronic
# PCS : Programming-Assignment-2

######################################
# Aim: To plot FM Waves!
######################################


# In[2]:


# import required packages
import numpy as np
import matplotlib.pyplot as plt


# In[25]:


# Frequency Modulation

# baseband signal:    m(t) = Am*cos(wm*t)
# carrier signal:     c(t) = Ac*cos(wc*t)
# FM signal:          φFM(t) = Ac*cos(wc*t + βsin(wm*t))
# Modulation Index: β = (kf * Am)/ fm

A_m = float(input("Enter Baseband Amplitude: "))  #1
f_m = float(input("Enter Baseband Frequency: "))  #50
A_c = float(input("Enter Carrier Amplitude: "))  #20
f_c = float(input("Enter Carrier Frequency: ")) #200
kf = float(input("Enter modulation sensitivity (kf): ")) #80

# signal generation
t = np.linspace(0, 100, 1000)
mod_index = (kf*A_m)/f_m
print()
print("Modulation index: " + str(mod_index))

# w_m = 2*pi*f_m, similar for w_c
baseband = A_m*np.cos(2*np.pi*f_m*t)
carrier = A_c*np.cos(2*np.pi*f_c*t)
frequency_modulation = A_c*np.cos((2*np.pi*f_c*t) + (mod_index*np.sin(2*np.pi*f_m*t)))

# plotting signals
plt.subplot(3,1,1)
plt.title("Baseband signal (m(t))" )
plt.plot(baseband,"green")
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.subplot(3,1,2)
plt.title("Carrier signal (c(t))" )
plt.plot(carrier, "red")
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.subplot(3,1,3)
plt.title("FM Modulated (φFM(t))" )
plt.plot(frequency_modulation, color="blue")
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(16, 11)
fig.suptitle("Frequency Modulation")

