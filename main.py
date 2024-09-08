import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
crimes['hour_normal'] = crimes['TIME OCC'].str[:2].astype(int)
plt.figure(figsize=(12,8))
v = sns.countplot(data=crimes, x='hour_normal',hue='Vict Sex')
plt.xlabel('Hour')
plt.ylabel('Count of crimes')
v.set_title('Crimes by hour')
plt.show()

peak_crime_hour = crimes['hour_normal'].value_counts().sort_values(ascending=False).index[0]
night_crimes = crimes[(crimes['hour_normal'] >= 22) & (4 < crimes['hour_normal'])]
peak_night_crime_location = night_crimes.groupby('AREA NAME').agg({'hour_normal': 'count'}).sort_values(by='hour_normal', ascending=False).index[0]
plt.figure(figsize=(12, 8))
g = sns.countplot(data=crimes, x='AREA NAME', hue='Vict Sex')
plt.xlabel('Area Name')
plt.ylabel('Count of crimes')
g.set_title('Crimes by Area Name')
g.set_xticklabels(g.get_xticklabels(), rotation=45)
plt.show()

age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
crimes['Vict Age Group'] = pd.cut(crimes['Vict Age'], bins=age_bins, labels=age_labels, right=True)
victim_ages = crimes['Vict Age Group'].value_counts().sort_values()

plt.figure(figsize=(12, 8))
h = sns.histplot(data=crimes, x='Vict Age Group',discrete=1,color='green', alpha=0.5)
h.set_title('Crimes per Age Group')
plt.xlabel('Victim Age Group')
plt.ylabel('Count of crimes')

plt.figure(figsize=(12, 8))
p = sns.kdeplot(data=crimes, x='Vict Age', hue='Vict Age Group')
p.set_title('Crimes per Age Group')
plt.xlabel('Victim Age Group')
plt.ylabel('Density of crimes')
plt.show()
