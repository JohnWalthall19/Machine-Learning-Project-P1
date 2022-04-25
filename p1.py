#!/bin/python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./ifood_df.csv.3")

row = dict(df.iloc[0])
print(row)
mnt = 0
for i in row:
    if i[0:3] == "Mnt":
        print(i, row[i])
        mnt += row[i]
print(mnt)

sns.jointplot( data=df, x="MntTotal", y="MntWines" )
plt.savefig("./MntWinesAndMntTotal.png");

"""
df = pd.read_csv("./bank-additional-balanced.csv")
education_levels = [ 'basic.4y', 'high.school', 'basic.6y', 'basic.9y', 'professional.course', 'unknown', 'university.degree', 'illiterate' ]

def int_education( education_level_string ):
    return education_levels.index( education_level_string )

df["i_education"] = df["education"].apply( int_education );

m_status = [ 'married', 'single', 'divorced', 'unknown' ]

def y_or_no_marital( row ):
    return m_status.index( row["marital"] ) + 4*(row["y"] == "yes")

df["color"] = df.apply( y_or_no_marital, axis=1 )
print(df)
print(df.dtypes)
print(df["marital"].unique())


#sns.jointplot( data=df, x="age", y="i_education", hue="y" )
#sns.jointplot( data=df, x="age", y="nr.employed", hue="y" )
#sns.jointplot( data=df, x="age", y="nr.employed", hue="color" )
sns.jointplot( data=df, x="age", y="color", hue="color" )
plt.savefig("./graph.png");
"""
