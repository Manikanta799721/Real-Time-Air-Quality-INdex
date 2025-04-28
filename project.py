import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/eswar/Downloads/Real Time Air Quality python.csv')
print(df.head())

#Bar Graph
plt.figure(figsize=(8, 5))
sb.countplot(data=df, y='pollutant_id', order=df['pollutant_id'].value_counts().index)
plt.title('Count of Observations per Pollutant Type')
plt.xlabel('Count')
plt.ylabel('Pollutant Type')
plt.show()

#Heatmap
columns_of_interest = ['latitude', 'longitude', 'pollutant_avg']
subset_df = df[columns_of_interest]
corr_matrix = subset_df.corr()
plt.figure(figsize=(8, 6))
sb.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap of Selected Air Quality Attributes')
plt.tight_layout()
plt.show()

#Histogram
plt.figure(figsize=(8, 5))
sb.histplot(df['pollutant_avg'], bins=30, kde=True)
plt.title('Distribution of Average Pollutant Levels')
plt.xlabel('Pollutant Average')
plt.ylabel('Frequency')
plt.show()

#scatterplot
plt.figure(figsize=(8, 5))
sb.scatterplot(data=df, x='longitude', y='latitude', hue='pollutant_id', alpha=0.7)
plt.title('Geographic Distribution of Pollutants')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Pollutant Type')
plt.show()

#boxplot
plt.figure(figsize=(8, 5))
sb.boxplot(data=df, x='pollutant_id', y='pollutant_avg')
plt.title('Pollutant Level Spread by Type')
plt.xlabel('Pollutant Type')
plt.ylabel('Pollutant Average')
plt.show()


pollutant_counts = df['pollutant_id'].value_counts()

# pie chart
plt.figure(figsize=(8, 8))
plt.pie(pollutant_counts, labels=pollutant_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Observations per Pollutant Type')
plt.axis('equal') 
plt.show()