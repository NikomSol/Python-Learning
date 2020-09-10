import pandas as pd
import numpy as np

# Read from file
df = pd.read_excel('data.xlsx',index_row=0)
# print(df)

#New row
df.loc[4]=[2,3]
# print(df)

# New column (position, name, data)
df.insert(2,'P*l',df['l']*df.P)

# print(df)

#filter by condition
high_P = df[df.P > 2]
# print(high_P)

#changes element
# high_P['P'][1] = 0
# print(high_P)

#merge data for column (data,merge type ,base column)
dfAll = df.merge(high_P,'left',on='l')
# print(dfAll)

# DF from numpy
data = np.zeros((2,2))
df = pd.DataFrame(data,index=['c','d'],columns=['a','b'])
# print(df)
# print(df['a']['c'])

# DF from numpy
data = np.zeros((2,2))
df = pd.DataFrame(data,columns=['a','b'])
# print(df)
# print(df['a'][1])

# DF from dict
data = {'a':[[1,1],1], 'b':[0,1]}
df = pd.DataFrame(data=data)
# print(df)

data = {'a': [np.array([1,2,3]),2],'b': [np.array([1,1]),3]}
df = pd.DataFrame(data=data)
# print(df)

data = {'a': np.array([[1,1],[1,1]]),'b': np.array([[1,1],[3,1]])}
# df = pd.DataFrame.from_dict(data, orient='index')
# print(df)

data = {'a': np.array([1,1]),'b': np.array([3,1])}
df = pd.DataFrame()
for i, key in enumerate(data.keys()):
    df.insert(i, key, [data[key]])

df.loc[4] = data


print(df)
