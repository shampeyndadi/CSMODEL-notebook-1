import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

pokemon_df = pd.read_csv('C:\\Users\\admin\Downloads\\4 - Exploring Pokemon Data - Blank\\pokemon.csv')

normal_pokemon_df = pokemon_df[pokemon_df['type_1'] == 'Normal']
normal_pokemon_df.hist('hp', bins=30, edgecolor='w', figsize=(8, 4))

mean_baseDefense_df = pokemon_df.groupby('type_1').agg({'defense' : ['mean', 'std']})
print(mean_baseDefense_df)

mean_sortedbaseDefense_df = mean_baseDefense_df.sort_values(('defense', 'mean'), ascending=False)
print(mean_sortedbaseDefense_df)

median_baseDefense_df = pokemon_df.groupby('type_1').agg({'defense': ['median']})
median_sortedbaseDefense_df = median_baseDefense_df.sort_values(('defense', 'median'), ascending=False)
print(median_sortedbaseDefense_df)

hp_atk_def = pokemon_df[['hp', 'attack', 'defense']]
hp_atk_def.corr()

hp_atk_def.plot.scatter(x='attack', y='defense', alpha=0.5)
plt.title('Relationship of Pokemon HP and Attack')
plt.show()