import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataframe = pd.read_excel("BlinkIT Grocery Data.xlsx")
print(dataframe.head())
def handleRate(value):
    value=str(value).split('/')
    value=value[0]
    return float(value)


dataframe['Sales']=dataframe['Sales'].apply(handleRate)
print(dataframe.head())
dataframe.info()
sns.countplot(x="Outlet Location Type", data=dataframe)
plt.xlabel("Outlet Type")
plt.show()
plt.figure(figsize=(6,4))
sns.countplot(x="Outlet Size", data=dataframe, order=["Small", "Medium", "High"], palette="Set3")
plt.title("Outlet Distribution by Size")
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x="Item Type", y="Sales", data=dataframe, estimator="mean", palette="coolwarm")
plt.title("Average Sales by Item Type")
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="Item Weight", y="Sales", hue="Item Fat Content", data=dataframe, palette="Set1")
plt.title("Sales vs Item Weight")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x="Item Visibility", y="Sales", hue="Outlet Size", data=dataframe, palette="Dark2")
plt.title("Sales vs Item Visibility")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(dataframe.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()



