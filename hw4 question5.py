#question 5 part 1
import matplotlib.pyplot as plt
import numpy as np
y=np.array([88,66,90,55,77])
mylabels=['Andy','Amy','James','Jules','Arthur']
plt.pie (y, labels = mylabels)
plt.title ('Students Grades')
plt.legend(bbox_to_anchor=(1.0,1.0), loc='upper left')
plt.show()

#question 5 part 2
import matplotlib.pyplot as plt
import numpy as np
x= np.array (['Jules','Amy','Arthur','Andy','James'])
y= np.array ([55,66,77,88,90])
plt.title('Students Grades')
plt.bar(x,y)
plt.show()