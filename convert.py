#!/usr/bin/python

# to convert alpha-al2o3 from primitive to converntional unit cell

f1=open('xred','r')
ff1=f1.readlines()
f1.close

g1=open('hex.xyz','w')



for i in range(10):
  aa=ff1[i].split()
  a1=float(aa[0])
  a2=float(aa[1])
  a3=float(aa[2])
  a4=aa[3]

  for ia1 in range(7):
   for ia2 in range(7):
     for ia3 in range(7) :
       aa1=a1+ia1-3
       aa2=a2+ia2-3
       aa3=a3+ia3-3


       b1=(aa1-2*aa2+aa3)/3
       b2=(aa1+aa2-2*aa3)/3
       b3=(aa1+aa2+aa3)/3
       b4=a4
       if 0<=b1<1 and 0<=b2<1 and 0<=b3 <1 :
          b1=str(b1)
          b2=str(b2)
          b3=str(b3)
          
          g1.write(b4+' '+b1+' ')
          g1.write(b2+' ')
          g1.write(b3+'\n')

g1.close()
