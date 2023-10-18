import pandas as pd
pd.set_option('display.max_columns', 8)
general = pd.read_csv('../files/test/general.csv')
parental = pd.read_csv('../files/test/prenatal.csv')
sports = pd.read_csv('../files/test/sports.csv')
print(general.head(20), parental.head(20), sports.head(20), sep='\n')