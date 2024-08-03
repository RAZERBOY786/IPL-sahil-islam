import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
ipls = pd.read_csv('C:/Users/MD Sahil Johan Islam/OneDrive/Desktop/c programming/data.csv')
print(ipl)
print(ipl)
print(ipl.isnull().sum())
ipl_cleaned = ipl.dropna()
ipl_filled = ipl.fillna(0)
print(ipl.describe())
print(ipl.head())
print(ipl.tail())
print(ipl.info())
print(ipl['toss_winner'].value_counts())

sns.histplot(x='toss_winner',data=ipls)
plt.show()

plt.plot(ipls='date')
plt.show()

sns.displot(x='date',data=ipls)
plt.show()

ipl= ipls[['toss_winner', 'toss_decision']].apply(lambda x: pd.factorize(x)[0])
corr = ipl.corr()
print(corr)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()

city= ipls['city'].value_counts()
city.plot(kind='bar')
plt.show()

sns.boxplot(ipls['city'])
plt.show()

sns.scatterplot(x='winner',y='winner',data=ipls,hue='winner')
plt.show()

sns.pairplot(ipls,hue='winner')
plt.show()