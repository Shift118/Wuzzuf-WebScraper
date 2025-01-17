from datetime import datetime, timedelta
import calendar
import os
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import re

def convert_relative_time(relative_time):
    now = datetime.now()

    if "day" in relative_time:
        days = int(relative_time.split()[0])
        return now - timedelta(days=days)

    elif "hour" in relative_time:
        hours = int(relative_time.split()[0])
        return now - timedelta(hours=hours)

    elif "month" in relative_time:
        months = int(relative_time.split()[0])
        year = now.year
        month = now.month - months

        if month <= 0:
            year -= 1
            month += 12

        return datetime(year, month, now.day)

    elif "minute" in relative_time:
        minutes = int(relative_time.split()[0])
        return now - timedelta(minutes=minutes)

    else:
        return None


def wuzzuf_scrap(web_link, file_name):
    # Lists to store
    job_title = []
    company_name = []
    location_name = []
    skills = []
    links = []
    time_posted = []
    converted_dates = []  # New list for converted dates

    page = 0

    while True:
        result = requests.get(f"{web_link[:-1]}{page}")
        src = result.content
        soup = BeautifulSoup(src, "lxml")

        TotalJobs = int(soup.find("strong").text)
        if page > TotalJobs // 15:
            print("End Reached Terminate")
            break

        job_titles = soup.find_all("h2", {"class": "css-m604qf"})
        company_names = soup.find_all("a", {"class": "css-17s97q8"})
        locations = soup.find_all("span", {"class": "css-5wys0k"})
        job_skills = soup.find_all("div", {"class": "css-y4udm8"})
        time_posts = soup.find_all(["div", "div"], class_=["css-do6t5g", "css-4c4ojb"])

        for i in range(len(job_titles)):
            job_title.append(job_titles[i].text)
            links.append(job_titles[i].find("a").attrs['href'])
            company_name.append(company_names[i].text[:-2])
            location_name.append(locations[i].text)
            skills.append(job_skills[i].text)
            time_str = time_posts[i].text
            time_posted.append(time_str)
            converted_dates.append(convert_relative_time(time_str))  # Convert and store the date

        page += 1

    job_types = ['Full Time', 'Hybrid', 'On-site', 'Remote', 'Freelance / Project', 'Shift Based']
    extracted_job_types = []
    cleaned_jobs = []

    for job in skills:
        job_type_pattern = '|'.join(re.escape(type_) for type_ in job_types)
        extracted_types = re.findall(job_type_pattern, job)

        if extracted_types:
            extracted_job_types.append(' , '.join(extracted_types))
            cleaned_job = job
            for type_ in extracted_types:
                cleaned_job = re.sub(re.escape(type_), '', cleaned_job, count=1)
            cleaned_job = cleaned_job.strip().replace('  ', ' ')
            cleaned_jobs.append(cleaned_job)
        else:
            extracted_job_types.append('')
            cleaned_jobs.append(job)

    skills = [i.replace(" · ", " , ") for i in cleaned_jobs]

    file_list = [job_title, company_name, converted_dates, time_posted, location_name, extracted_job_types, skills,
                 links]  # Updated list
    exported = zip_longest(*file_list)

    directory = "Jobs"
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(f"{directory}/{file_name}.csv", "w", newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(
            ["Job Title", "Company Name", "Date", "Time Posted", "Location Name", "Job Type", "Skills",
             "Links"])  # Updated header
        wr.writerows(exported)
