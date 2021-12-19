import requests
from bs4 import BeautifulSoup
import re

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="card-content")

for job_element in job_elements:
	title = job_element.find("h2", class_="title").text.strip()
	company = job_element.find("h3", class_="company").text.strip()
	location = job_element.find("p", class_="location").text.strip()
	date_published = job_element.find("time", attrs={"datetime": re.compile(r".*")}).text.strip()
	job_posting = (title, company, location, date_published)

	print(job_posting)