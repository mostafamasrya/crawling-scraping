# pip install requests
# pip install beautifulsoup4
# pip install lxml
# pip install 
from os import link
from unittest import result
import requests
import csv
from bs4 import BeautifulSoup
from itertools import zip_longest


# 2 .use requests to fetch our page

result=requests.get("https://wuzzuf.net/search/jobs/?q=python+&a=navbl")


# 3. save the content in src variable

src=result.content
# print(src)

# 4. using beautiful soup with parser lxml which allow me to process on data

soup=BeautifulSoup(src,"lxml")

# print(soup)



# 5. finding elements which contain info we need .
# job title , skills ,company name , location

job_titles= soup.find_all("h2",{"class":"css-m604qf"})


company_names=soup.find_all("a" ,{"class":"css-17s97q8"})

locations=soup.find_all("span",{"class":"css-5wys0k"})

skills=soup.find_all("div",{"class":"css-y4udm8"})
# print(skills[0].text)




# 6. get text from the content we got above and append them to our lists
job_title=[]
company_name=[]
location=[]
skill=[]
links=[]



# for loop 

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    links.append(job_titles[i].find("a").attrs['href'])
    company_name.append(company_names[i].text)
    location.append(locations[i].text)
    skill.append(skills[i].text)


# print(job_title)

print(links[1])


# ===============================================================================

# using links to get salary and other info which in (details page)

# salaries=[]
# # for link in links:
# result=requests.get(f"https://wuzzuf.net/{links[1]}")
# src=result.content
# soup=BeautifulSoup(src,"lxml")

# my_salary = soup.find("h2",{"class":"css-1u59jur"})
# print("here is len")
# print(my_salary)
#     # salaries.append(my_salary.text.strip())
    
# ==================================================================================

# 7. create csv file and store our data on 

# we need to use zip_longest to unpacking my lists 

file_list = [job_title , company_name , location , skill ]
exported_data=zip_longest(*file_list)

with open("D:/programming/ITI/crawling/wussufinfo.csv","w") as myfile:
    wr=csv.writer(myfile)
    wr.writerow(["job title","company name","location","skills" ])
    wr.writerows(exported_data)

