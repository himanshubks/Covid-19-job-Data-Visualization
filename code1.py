pip install matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset into a Pandas DataFrame (replace 'data.csv' with your actual file)
df = pd.read_csv('data.csv')

# Line Chart: Total Jobs Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Total Jobs', data=df)
plt.title('Total Jobs Over Time')
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Total Jobs')
plt.tight_layout()
plt.show()

# Bar Chart: Top Hiring Companies
top_hiring_companies = df.groupby('Company')['Jobs'].sum().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_hiring_companies.values, y=top_hiring_companies.index, palette='viridis')
plt.title('Top Hiring Companies')
plt.xlabel('Total Jobs')
plt.ylabel('Company')
plt.tight_layout()
plt.show()
