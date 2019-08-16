#!/usr/bin/python
# this is to calculate U(G) by integration in unit cell.

import math
f1=open('_k37_b2','r')
ff1=f1.readlines()
f1.close()

ugr=0
ugi=0
for i in range(368640) :
  fa=2*3.1415926/3.0479
  k=[0.5*fa,0.5*1.73205*fa,0*fa]
  G=[0,0,0]
  r=ff1[i].split()
  rr=[float(r[0]),float(r[1]),float(r[2]),float(r[3]),float(r[4])]
  phase=(k[0]+G[0])*rr[0]+(k[1]+G[1])*rr[1]+ (k[2]+G[2])*rr[2]
  phase-=3.1415926
  b1=float(rr[3])*math.cos(-phase)-float(rr[4])*math.sin(-phase)
  b2=float(rr[3])*math.sin(-phase)+float(rr[4])*math.cos(-phase)
  ugr+=b1
  ugi+=b2
print ugr/368640
print ugi/368640  
