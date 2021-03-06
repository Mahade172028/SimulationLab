# -*- coding: utf-8 -*-
"""Random number Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10w8f7gxGODvG9_7ZHX4SaJc9CIn9Aw0S
"""

#initiazing the component
Z1=[12,7]
Z2=[3,5]
Z3=[2,7]
U1=[]
U2=[]
U3=[]
U_main=[]

#initializing the require function

def fun_z1():
  return (13*Z1[-1]+Z1[-2]+3)%16

def fun_z2():
  return (12*(Z2[-1]**2)+13*Z2[-2])%17

def fun_z3():
  return ((Z3[-1]**3)+Z3[-2])%15


def plot():
  #ploting the U array
  import matplotlib.pyplot as plt
  import numpy as np
  plt.hist(U_main, bins = 20)
  plt.show()

n_array=[100,1000,5000]
#executing recursive generator
#n=int(input("Enter N:"))
for n in n_array:

  for i in range(0,n):
    z1=fun_z1()
    Z1.append(z1)
    z2=fun_z2()
    Z2.append(z2)
    z3=fun_z3()
    Z3.append(z3)

    u1=z1/16
    U1.append(u1)
    u2=z2/17
    U2.append(u2)
    u3=z3/15
    U3.append(u3)

    u_main=(u1+u2+u3)
    tmp=u_main
    u_main=u_main-int(tmp)
    U_main.append(u_main)
  plot()
  Z1=[12,7]
  Z2=[3,5]
  Z3=[2,7]
  U1=[]
  U2=[]
  U3=[]
  U_main=[]