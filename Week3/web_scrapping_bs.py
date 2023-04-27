from bs4 import BeautifulSoup
import requests

request_page = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')

print(request_page)
link = BeautifulSoup(request_page.text, 'html.parser')
dataset,header_list = [], []
main = link.find_all('div', attrs = {'id': 'contentDiv'})
print(main[0].find_all('table'))
for obj in main:
    print(obj.find_all('table'))0
    # if len(obj.find_all('table') > 0):
    #     break
    if len(obj.find_all('table')) > 0:
        for table_index in obj.find_all('table'):
            if len(table_index.find_all('tr'))>0:
                for table_trs in table_index.find_all('th'):
                    print(table_trs.get_text())
                    header_list.append(table_trs.get_text())
                break
        break

print(header_list)