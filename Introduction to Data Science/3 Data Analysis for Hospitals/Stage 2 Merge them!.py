import pandas as pd
pd.set_option('display.max_columns', 8)
general = pd.read_csv('../files/test/general.csv')
parental = pd.read_csv('../files/test/prenatal.csv')
sports = pd.read_csv('../files/test/sports.csv')
parental.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
merged = pd.concat([general, parental, sports], ignore_index=True).drop(columns=['Unnamed: 0'])
print(merged.sample(n=20, random_state=30))