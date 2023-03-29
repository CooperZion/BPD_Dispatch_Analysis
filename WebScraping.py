import request
from bs4 import BeautifulSoup
import csv

lst_31 = [1, 3, 5, 7, 8, 10, 12]
lst_30 = [4, 6, 9, 11]
date_lst = []
html_date_lst = []

for i in range(12):
    if i+1 in lst_31:
        for j in range(31):
            date_lst.append(f'{i + 1}-{j + 1}')
            month = str(i+1)
            day = str(j+1)
            html_date_lst.append(f'{month.zfill(2)}.{day.zfill(2)}.2022')
    elif i+1 in lst_30:
        for j in range(30):
            month = str(i + 1)
            day = str(j + 1)
            date_lst.append(f'{i + 1}-{j + 1}')
            html_date_lst.append(f'{month.zfill(2)}.{day.zfill(2)}.2022')
    else:
        for j in range(28):
            month = str(i + 1)
            day = str(j + 1)
            date_lst.append(f'{i + 1}-{j + 1}')
            html_date_lst.append(f'{month.zfill(2)}.{day.zfill(2)}.2022')

    URL_lst = []

    for item in html_date_lst:
        URL = f'https://www.burlingtonvt.gov/sites/default/files/{item}.pdf'
        URL_lst.append(URL)



# with open("ODs.csv", 'w', newline='') as outfile:
#         csv_writer = csv.writer(outfile)
#         csv_writer.writerow(lst)
