from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


def tocsv(csv_file, dict):
    try:
        with open(csv_file, 'w', newline='', encoding='euc-kr') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict:
                writer.writerow(data)
    except IOError:
        print('I/O err')


url = 'https://wis.hufs.ac.kr/src08/jsp/lecture/LECTURE2020L.jsp'

campus = input("Campus: ")
#division = input("Division: ")
major = input("Major: ")

if campus == '글로벌':
    url += '?campus_sect=H2&ag_crs_strct_cd='
    if major == '컴전':
        url += 'ATIA1_H2'
    elif major == 'GBT':
        url += 'ARDA1_H2'
    elif major == '통계':
        url += 'ASHB2_H2'
    elif major == '중통':
        url += 'AORA2_H2'
    elif major == '정통':
        url += 'ATFB2_H2'

'''   
elif campus == '서울':
    url += '?campus_sect=H1&ag_crs_strct_cd='
    if major == ''
'''

html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


td = [n.text.strip().replace('  ', '').replace('\r\n', '').replace('\xa0', '').replace('\n', '')
      for n in soup.find('div', class_="table write margin_top10 align_center font-size11").find_all('td')]

result = []
csv_columns = ['번호', '과목', '교수', '시간', '신청인원']

no, sub, prof, time, num = 0, 4, 11, 14, 15
no_tmp, sub_tmp, prof_tmp, time_tmp, num_tmp = "", "", "", "", ""

for i, data in enumerate(td):
    if i == no:
        no_tmp = data
        no += 17
    elif i == sub:
        sub_tmp = data
        sub += 17
    elif i == prof:
        prof_tmp = data
        prof += 17
    elif i == time:
        time_tmp = data
        time += 17
    elif i == num:
        num_tmp = data
        num += 17
        result.append({'번호': no_tmp, '과목': sub_tmp, '교수': prof_tmp, '시간': time_tmp, '신청인원': num_tmp})

tocsv("reg_result.csv", result)

