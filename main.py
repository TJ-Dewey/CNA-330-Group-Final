import pandas as pd
from sqlalchemy import create_engine
import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Connect to database
# You may need to edit the connect function based on your local settings.
#This Can connect to local .csv file or website from github
data = "https://raw.githubusercontent.com/Francisco-222/SQL-FINAL/main/nba%20players.csv"
# data =  connect from pd.read_csv("nba players.csv")
#Prints columns and cleans up empty lines
data=pd.read_csv(data)
print(data.columns)    # prints columns from csv
data = data.dropna()     # delete all empty lines
data = data.where(pd.notnull(data), None)     # Aldf'so delete the empty lines
##you can google to run panda as console
##### PLot #### will show the avarages of age and weight of NBA players
df = pd.read_csv("C:\\Users\\Francisco\\Desktop\\nba players.csv") #change for you path location
subjects = ['Age', 'Weight', ]
dataset = df.groupby('Position')[subjects].mean()
indx = np.arange(len(subjects))
score_label = np.arange(50, 300, 50)
PG_means = list(dataset.T['PG'])
SF_means = list(dataset.T['SF'])
bar_width = 0.35
fig, ax = plt.subplots()
barPG = ax.bar(indx - bar_width/2, PG_means, bar_width, label='PG_means')
barSF = ax.bar(indx + bar_width/2, SF_means , bar_width, label='SF_means')
# inserting x axis label
ax.set_xticks(indx)
ax.set_xticklabels(subjects)
# inserting y axis label
ax.set_yticks(score_label)
ax.set_yticklabels(score_label)
# inserting legend
ax.legend()
def insert_data_labels(bars):
   for bar in bars:
      bar_height = bar.get_height()
      ax.annotate('{0:.0f}'.format(bar.get_height()),
         xy=(bar.get_x() + bar.get_width() / 2, bar_height),
         xytext=(0, 3),
         textcoords='offset points',
         ha='center',
         va='bottom'
      )
insert_data_labels(barPG)
insert_data_labels(barSF)
plt.show()
