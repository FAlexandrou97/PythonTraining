import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# matplotlib.use('TkAgg')

df = pd.read_csv('Pokemon.csv', encoding="ISO-8859-1", index_col=0)
print(df.head())

sns.lmplot(x='Attack', y='Defense', data=df)
plt.show()
plt.close()

sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False,  # Remove middle line
           hue='Stage')  # Evolution stage color

# Set x,y limits using matplotlib
plt.ylim(0, None)
plt.xlim(0, None)
plt.show()
plt.close()


stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
sns.boxplot(data=stats_df)
plt.show()
plt.close()


sns.set_style('whitegrid')

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

sns.violinplot(x='Type 1', y='Attack', data=df,
               palette=pkmn_type_colors) # Set color palette
plt.show()
plt.close()

sns.swarmplot(x='Type 1', y='Attack', data=df,
              palette=pkmn_type_colors)
plt.show()
plt.close()

sns.kdeplot(df.Attack, df.Defense)
plt.show()
plt.close()





