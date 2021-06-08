"""Demo of scraping a web site
"""

import requests
from bs4 import BeautifulSoup

# URL = "https://www.codefellows.org/courses/code-400/"
URL = "https://testing-www.codefellows.org/course-calendar/?filters=code-javascript-401,code-python-401,code-java-401,code-dotnet-401,ops-cybersecurity-401"

page = requests.get(URL)

# print(page.content)

soup = BeautifulSoup(page.content, "html.parser")


headings = soup.find_all("h1")

course_titles = [heading.text for heading in headings[2:]]


uniques = set(course_titles)

# for heading in headings[2:]:
#     uniques.add(heading.text)

sorted_titles = sorted(uniques)

for course in sorted_titles:
    print(course)
