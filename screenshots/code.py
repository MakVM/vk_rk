import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("ticks",{'axes.grid' : True})

base = pd.read_csv('data.csv')
base['TRACK_ID'] = base['TRACK_ID'].apply(lambda x: x.split('-')[-1] + ':') + base['OBJECT_TYPE']
base.drop(['OBJECT_TYPE'], axis=1, inplace=True)

line, ax = plt.subplots(figsize=(20.48, 20.48))
ax = sns.lineplot(data=base, x='X', y='Y', hue='TRACK_ID', palette='husl')
ax.set_title("Визуализация дорожной сцены", fontsize=25)
line.savefig("scene.png")