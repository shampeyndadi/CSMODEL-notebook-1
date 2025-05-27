import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

pokemon_df = pd.read_csv('C:\\Users\\admin\Downloads\\4 - Exploring Pokemon Data - Blank\\pokemon.csv')

#pokemon_df.info()

#Question 1: 1028
#Question 2: 48

#print(pokemon_df.tail(1)[['name', 'type_1', 'type_2']])

#Question 3: Poison, Dragon (??)

type_count_df = pokemon_df['type_1'].value_counts()

type_count_df.plot.barh(figsize=(6,7)).invert_yaxis()
plt.xlabel('Primary Type')
plt.ylabel('Count')
plt.title('Pokemon count per primary type')

#plt.show()

#Question 4: Water, Normal, Grass
pokemon_df.hist('hp', bins=30, edgecolor='w', figsize=(8, 4))
plt.show()   # explicit call to show the chart (not needed with the matplotlib inline command)

print(pokemon_df['hp'])

print(pokemon_df[(pokemon_df['type_1'] == 'Normal') & (pokemon_df['generation'] <= 5)]['hp'].agg('median'))

print(pokemon_df.groupby('type_1').agg({'attack': 'median'}).sort_values('attack', ascending=False))

print(pokemon_df.groupby('type_1').agg({'defense' : ['mean', 'std']}))

print(pokemon_df.groupby('type_1').agg({'defense' : ['mean', 'std']}).sort_values(('defense', 'mean'), ascending=False))

print(pokemon_df.groupby('type_1')['defense'].median().sort_values(ascending=False))

pokemon_df.boxplot('defense', by='type_1', figsize=(15, 10))

pokemon_df.plot.scatter(x='attack', y='defense', alpha=0.5)
plt.title('Relationship of Attack and Defense')


plt.show()