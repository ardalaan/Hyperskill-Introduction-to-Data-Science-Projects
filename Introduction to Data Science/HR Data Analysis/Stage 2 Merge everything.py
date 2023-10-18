import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    A_office_data = pd.read_xml('../Data/A_office_data.xml')
    B_office_data = pd.read_xml('../Data/B_office_data.xml')
    hr_data = pd.read_xml('../Data/hr_data.xml')
    hr_data.set_index('employee_id', inplace=True)
    A_office_data.index = ['A' + str(eoi) for eoi in A_office_data['employee_office_id']]
    B_office_data.index = ['B' + str(eoi) for eoi in B_office_data['employee_office_id']]
    merged = pd.concat([A_office_data, B_office_data]).merge(hr_data, left_index=True, right_index=True, how='left',
                                                             indicator=True)
    merged = merged[merged._merge == 'both'].drop(columns=['employee_office_id', '_merge']).sort_index()
    print(list(merged.index), list(merged.columns), sep='\n')