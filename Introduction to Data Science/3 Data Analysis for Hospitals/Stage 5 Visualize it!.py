import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', 8)
general = pd.read_csv('../files/test/general.csv')
parental = pd.read_csv('../files/test/prenatal.csv')
sports = pd.read_csv('../files/test/sports.csv')
parental.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)
merged = pd.concat([general, parental, sports], ignore_index=True).drop(columns=['Unnamed: 0'])
merged.dropna(how="all", inplace=True)
merged.replace(to_replace={'gender': {'female': 'f', 'woman': 'f', 'male': 'm', 'man': 'm'}}, inplace=True)
merged.fillna(value={'gender': 'f', 'bmi': 0, 'diagnosis': 0, 'blood_test': 0, 'ecg': 0, 'ultrasound': 0, 'mri': 0, 'xray': 0, 'children': 0, 'months': 0}, inplace=True)
bins = [0, 15, 35, 55, 70, 80]
plt.hist(merged.age, bins=bins)
plt.show()
print('The answer to the 1st question: 15-35')
labels = merged.diagnosis.value_counts().index
plt.pie(merged.diagnosis.value_counts(), labels=labels)
plt.show()
print('The answer to the 2nd question: pregnancy')
heights = [merged.query(f"hospital == '{hospital}'").height for hospital in merged.hospital.unique()]
plt.violinplot(heights)
plt.show()
print("The answer to the 3rd question: It's because the patients in the third hospital are athletes and therefor"
      "are relatively taller than the average of the society. This factor can't explain the drastic difference between "
      "the data from different hospitals though. The difference in units of measurements is most likely the culprit"
      " here.")