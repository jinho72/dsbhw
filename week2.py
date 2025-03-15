#Define two custom numpy arrays, say A and B. Generate two new numpy arrays by stacking A and B vertically and horizontally.

import numpy as np

A = np.array([3,4,5])
B = np.array([6,7,8])
c = np.vstack((A,B))


#Find common elements between A and B. [Hint : Intersection of two sets]

common = intersect1d(A,B)

#Extract all numbers from A which are within a specific range. eg between 5 and 10. [Hint: np.where() might be useful or boolean masks]

np.where(A > 5, A < 10)



#Filter the rows of iris_2d that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0








#From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).\


import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')




#Replace missing values in Min.Price and Max.Price columns with their respective mean.




#df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')



#How to get the rows of a dataframe with row sum > 100?



#df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))