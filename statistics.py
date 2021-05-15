import matplotlib.pyplot as plt
import pandas
from scipy import stats

df = pandas.read_csv("Datalab.csv")
print(df)

df['experiments'].plot(kind='bar')

df1 = pandas.DataFrame(data={
    'df': df['experiments'],
})
df1.plot.kde()
plt.show()

d1 = df1['df']
print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=len(d1)))

