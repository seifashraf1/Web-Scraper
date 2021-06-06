#Simple Web Scarper to get jobs posted not more than a day ago with filtering option
from bs4 import BeautifulSoup
import requests
import time

print("Enter some skill that you are unfamiliar with")
unfamiliar_skill = input("> ")
print ("Filtering Out", unfamiliar_skill+"....")

def findJob():
    #response 200 (request is done successfully)
    html_file = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_file, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):     #loops with adding index to each job
        datePosted = job.find('span', class_ = 'sim-posted').text #start with data publised cuz its my priority, if cond met keep scrap, not met so dont
        if 'few' in datePosted:  
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '') #replace here just replace spaces with nothing to avoid empty spacing
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']   
            if unfamiliar_skill not in skills:
                with open (f'posts/{index}.txt', 'w') as f:
                    f.write (f"Company Name: {company_name.strip()}\n")
                    f.write (f"Skills: {skills.strip()}\n")
                    f.write (f"More Info: {more_info}\n")
                print (f"File Saved {index}")
        

if __name__ == '__main__':
    while True:
        findJob()
        waitingTime = 10        #in secs 
        print ("Updating in", waitingTime, "Minutes....")
        time.sleep(waitingTime * 60)
