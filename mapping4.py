import pandas as pd

# Create an empty list to store the data
data = []

for a in range(1, 4):
    df = pd.read_html('https://ngodarpan.gov.in/index.php/home/statewise_ngo/23097/27/' + str(a) + '?per_page=100')
    df1 = df[0]
    data.append(df1)

# Concatenate the list of DataFrames into a single DataFrame
consolidated_data = pd.concat(data, ignore_index=True)

# Save the data to an Excel file
consolidated_data.to_excel('tab1.xlsx', index=False)
