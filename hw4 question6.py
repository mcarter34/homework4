#question 6
import numpy as np
import matplotlib.pyplot as plt
#subplot1
x1= np.array([5,10,15,20])
y1= np.array([0,1,2,3])
x2= np.array([5,10,15,20])
y2= np.array([4,5,6,7])
plt.subplot(2, 3, 1)
plt.plot(x1,y1,x2,y2)
plt.title ('plot 1', fontsize=10)

#subplot2
x=np.array (['A','B','C','D'])
y=np.array ([2,4,8,6])
plt.subplot(2, 3, 2)
plt.bar(x,y)
plt.title ('plot 2', fontsize=10)

#subplot3
y=np.array([10,40,15,35])
mylabels=['other','cats','fish','dogs']
plt.subplot(2, 3, 3)
plt.pie (y, labels = mylabels)
plt.title ('plot 3', fontsize=10)

#subplot 4
x= np.array ([10,20,30,40])
y= np.array ([12,14,16,18])
plt.subplot(2, 3, 4)
plt.grid()
plt.plot(x, y)
plt.title('plot 4',fontsize=8)

#subplot 5
x= np.array([5,7,8,7,2,17,2,9])
y= np.array ([60,86,103,87,94,78,77,85])
plt.subplot(2, 3, 5)
plt.scatter(x,y)
plt.title('plot 5',fontsize=8)

#subplot 6
x= np.random.normal(123, 90, 321)
plt.subplot (2,3,6)
plt.hist(x)
plt.title('plot 6', fontsize=10)
plt.show()