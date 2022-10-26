import os
import time
from bs4 import BeautifulSoup
import requests


familar_skills = []
n = int(input("Enter number of skills you wish to input : "))
# we get number of skills we need to match

for i in range(0, n):
    ele = input()
  
    familar_skills.append(ele)
# here we get those skills in a list

print("enter the url of *timesjobs.com search result* or enter 0 if you wish to search defualt (Information Technology)")

xurl =input()
if(xurl=='0'):
    xurl = 'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'

directory = "matches"
ppath = os.getcwd()
dpath = os.path.join(ppath, directory)
if not os.path.exists(dpath):
    os.makedirs(dpath)

# here we get create matches directory if it already does not exists

def find_job():
    match = 0
    html_text = requests.get(xurl).text #get html content of webpage
    soup = BeautifulSoup(html_text, 'lxml') 
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx' ) 
    for index,job in enumerate(jobs) :
        published_date = job.find('span' , class_ = 'sim-posted').span.text
        if 'today' in published_date:
            compay_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            skills_string = str(skills).strip() 
            list_skills = list(skills_string.split(","))

            more_info = job.header.h2.a['href']

            #we get matches from html webpage

            if any(x in list_skills for x in familar_skills):
                with open( f'matches/{match}.txt', 'w' ) as f:
                    f.write(f"Company Name :  {compay_name.strip()} \n")
                    f.write(f"skills required :  {skills.strip()} \n")
                    f.write(f"link :  {more_info.strip()}")
                    match = match + 1
            # store matches in matches directory
        
if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

# our timer function which runs the script agian after 10 minutes