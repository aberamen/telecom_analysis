import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
df = pd.read_csv('data/processed/telecom_data.csv')

# Replace missing values
df.fillna(df.mean(), inplace=True)

# Basic metrics
print(df.describe())

# Univariate analysis
sns.histplot(df['total_data'], bins=50, kde=True)
plt.title("Distribution of Total Data Volume")
plt.savefig('output/visualizations/univariate_total_data.png')
plt.show()
