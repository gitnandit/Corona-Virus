import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mplcursors

data_frame = pd.read_csv('district_level_latest.csv')
data_frame.shape
data_frame.describe()

data_frame.describe()
data_frame.values

df = pd.DataFrame(data_frame, columns=['State', 'Confirmed', 'Active', 'Deceased', 'Recovered'])
print(df)
a = df.sort_values('Active', ascending=False)
print(a)

sns.set()

graph = sns.barplot(x='Active', y='State', data=df)
graph.set_title("Corona Virus Plot")
mplcursors.cursor(hover=True)
plt.xlabel('Active')
plt.ylabel('State')

# plt.title('Corona Report')
plt.show()
