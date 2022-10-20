#question 1 part 1
import numpy as np
integers = np.array ([[1,2,3,4],[5,6,7,8],[9,10,11,12]])*2
print(integers)

#question 1 part 2
import numpy as np
integers= np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
for row in integers:
    for column in row:
        print(column, end=' ')
    print ()

#question 1 part 3
import numpy as np
integers= np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
for i in integers.flat:
    print (i,end=' ')