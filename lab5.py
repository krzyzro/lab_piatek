from numpy import genfromtxt
import matplotlib.pyplot as plt
import random
import math

dane1=genfromtxt('data1.csv',delimiter='|')
dane2=genfromtxt('data2.csv',delimiter='|')

x1=[]
y1=[]
x2=[]
y2=[]

for i in dane1:
    x1.append(i[0])
    y1.append(i[1])

for y in dane2:
    x2.append(y[0])
    y2.append(y[1])




priori1=len(x1)/(len(x1)+len(x2))
priori2=len(x2)/(len(x1)+len(x2))



x3=random.uniform(0.5, 2.5)
y3=random.uniform(2, 6)

punkt1=0
punkt2=0
print('punkt',x3,y3)
a=1
while((punkt1+punkt2)==0):
    punkt1 = 0
    punkt2 = 0


    for i in range (len(dane1)):

        print('czerwon',x1[i],y1[i],abs((x3 - x1[i]) ** 2 + (y3 - y1[i]) ** 2))
        if ((abs((x3-x1[i])**2+(y3-y1[i])**2))<=a*a):
            punkt1+=1
            print("TAK-CZERWONE")


    for i in range (len(dane2)):
        print('zielone', x2[i], y2[i],abs((x3 - x2[i]) ** 2 + (y3 - y2[i]) ** 2))
        if ((abs((x3-x2[i])**2+(y3-y2[i])**2))<=a*a):
            punkt2+=1
            print("TAK-ZIELONE")


    print('czer',punkt1,'ziel', punkt2,a)
    print('--------------------------')
    if ((punkt1+punkt2)==0):
        a += 0.1


posteriori1=punkt1/len(dane1)
posteriori2=punkt2/len(dane2)

prawdop1=priori1*posteriori1
prawdop2=priori2*posteriori2



print("Prawdopodobieństwo czerwonych wynosi:",round(prawdop1,3),"(A priori:",round(priori1,3),'a posteriori:',round(posteriori1,3),")")
print("Prawdopodobieństwo zielonych wynosi:",round(prawdop2,3),"(A priori:",round(priori2,3),'a posteriori:',round(posteriori2,3),")")
fig,ax=plt.subplots()


plt.plot(x1, y1, 'ro',color='red')
plt.plot(x2, y2, 'ro',color='green')
if (prawdop1>prawdop2):
    plt.plot(x3, y3, 's',color='red')
else:
    plt.plot(x3, y3, 's', color='green')
circle = plt.Circle((x3, y3), radius=a, color='black',fill=False)
ax.add_artist(circle)


plt.show()
