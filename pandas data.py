import pandas as pd

# Read from file
df = pd.read_excel('data.xlsx',index_row=0)
print(df)

# New column (position, name, data)
df.insert(2,'P*l',df['l']*df.P)
print(df)

#filter by condition
high_P = df[df.P > 2]
print(high_P)

#changes
high_P['P'][1] = 0
print(high_P)

#merge
dfAll = df.merge(high_P,'left',on='l')
print(dfAll)