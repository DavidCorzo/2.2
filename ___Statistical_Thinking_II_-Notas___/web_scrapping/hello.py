import bs4 as bs
from bs4 import Comment
import urllib.request
from os import listdir
from collections import OrderedDict
from pprint import pprint
import xlsxwriter

workbook = xlsxwriter.Workbook('write_data.xlsx')
worksheet = workbook.add_worksheet()

def search_t1(soup):
    data = []
    table = soup.find(id='t1')
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values
    return data


persons = [["Name","Gender","Age","House num","last smoking status","sober test score","after alcohol","after canabis","URL"]]

for i in [html for html in listdir('htmls') if '.html' in html]:
    # 1: name, 2: gender, 3: age, 4: house num, 5: last smoking status, 6: sober test score, 7: after alcohol, 8: after canabis
    temp = [None,None,None,None,None,None,None,None,None] 
    with open('htmls/'+i, 'r') as f:
        contents = f.read()
        f.close()
        soup = bs.BeautifulSoup(contents, features="html5lib")

    # append the title
    # print(soup.find(id='title').contents[0])
    temp[0] = soup.find(id='title').contents[0] # gets the person name

    # get the gender, age, 
    data = search_t1(soup)
    # print(temp[0])
    # print(data)
    # print("-"*30)
    # get gender
    temp[1] = "F" if "Female" in data[1][0] else "M"
    temp[2] = data[2][0].replace(' years old','') # gets age
    if 'Lives in' in data[5][0]:
        temp[3] = data[5][0].split()[-1] # gets house number 
    elif 'Lives in' in data[6][0]:
        temp[3] = data[6][0].split()[-1] # gets house number 
    
    # get last smoking status
    last_smoking_status = None
    for ii in data:
        for iv in ii:
            if 'Light smoker' in iv:
                last_smoking_status = iv
            elif 'Nonsmoker' in iv: 
                last_smoking_status = iv
            elif 'Moderate smoker' in iv:
                last_smoking_status = iv
    if last_smoking_status == None: 
        last_smoking_status = "Never smoked"
    temp[4] = last_smoking_status

    # get sober test result
    counter = 0
    tasks   = soup.findAll("div", {"class": "taskresulttask"})
    for ii in tasks: 
        tasks[counter] = ii.contents
        counter += 1
    tasks = [i[0] for i in tasks[:-1]]

    results = soup.findAll("div", {"class": "taskresultresult"})
    counter = 0
    for ii in results: 
        results[counter] = ii.contents
        counter += 1
    results = [i[0].replace(' correct','').split('/')[0] for i in results]

    canabis,vodka, counter = None, None, 0
    for i in tasks:
        if 'Vodka' in i:
            vodka = counter
        elif 'Tea Cannabis' in i: 
            canabis = counter
        counter += 1
    # print(vodka,canabis)
    temp[5] = results[2]
    if vodka > canabis: # vodka was first 
        temp[6] = results[1]
        temp[7] = results[0]
    else: 
        temp[6] = results[0]
        temp[7] = results[1]

    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    for c in comments:
        c.extract()
        temp[8] = c.replace(' saved from url=(0056)','')

    persons.append(temp)

for i in persons:
    print(i)
row_counter = 0
for row in persons:
    col_counter = 0
    for col in row:
        worksheet.write(row_counter, col_counter, col)
        col_counter += 1
    row_counter += 1

workbook.close()

# source = urllib.request.urlopen('file:///D:/___UFM-Cursos___/4_Semestre-[Julio-Noviembre-2020]/____SumaDeCursosUFM2.2____/___Statistical_Thinking_II_-Notas___/htmls/web_scrapping/Maxine%20Page.html').read()

# soup = bs.BeautifulSoup(source,features="html5lib")

# print(soup.find(id="title"))
# # print(soup.find_all("div", {"id": "title"}))
