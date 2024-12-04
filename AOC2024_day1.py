import pandas as pd
df1 = pd.read_csv('dayinput.csv')

df1[['list1', 'list2']] = df1['list1'].str.split(pat=' ', n=1, expand=True)

df1['list1'] = df1['list1'].astype(int)
df1['list2'] = df1['list2'].astype(int)

df1 = df1.reset_index(drop=True)

df1['list1'] = sorted(df1['list1'])
df1['list2'] = sorted(df1['list2'])

df1['diff'] = abs(df1['list1'].astype(int) - df1['list2'].astype(int))

print(f"Sum of differences by sorted values: {sum(df1['diff'])}")

num_unique = df1['list2'].value_counts()

df1['similarity'] = df1['list1'].map(num_unique).fillna(0).astype(int)

df1['similarity_score'] = df1['list1'] * df1['similarity']

print(f"Sum of similarity scores: {sum(df1['similarity_score'])}")
