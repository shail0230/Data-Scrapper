This is a Python project that scrapes data from a website (https://ngodarpan.gov.in) using the pandas library. It retrieves information about NGOs (non-governmental organizations) from multiple pages and consolidates it into a single Excel file.

The project utilizes the pandas library to read HTML tables from the website and extract relevant data. It iterates over multiple pages, retrieves the data from each page, and stores it in a list. The list of DataFrames is then concatenated into a single DataFrame.

Finally, the consolidated data is saved to an Excel file named "tab1.xlsx" for further analysis or usage.
