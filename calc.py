import pandas
from datetime import datetime
import matplotlib.pyplot as plt


df = pandas.read_csv('./persons.csv')

df_grp = df.groupby('date').count()

x = df_grp.index.values
y = df_grp.name.values

print(x)
print(y)

plt.bar(x,y)
plt.ylabel('some numbers')
plt.show()