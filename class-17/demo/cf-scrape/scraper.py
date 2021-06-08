"""
Demo of scraping Code Fellows Courses
"""

###############
# step 1
###############

# import bs4
# import requests

# URL = "https://www.codefellows.org/courses/code-400/"
# page = requests.get(URL)

# print(page.content)


###############
# step 2
###############

# Move import to top of course
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(page.content, "html.parser")


###############
# step 3
###############

# results = soup.find(class_="course-details")

# print(results.prettify())


###############
# step 4
###############

# titles = results.find_all("h3")

# print(titles)

###############
# step 5
###############
# for title in titles:
#     print(title.text)


###############
# step 6
###############

# find_all is so common there's a shortcut
# anchors = results("a")

# print(type(anchors))


###############
# step 7
###############

# ResultSets are iterable and can be used in comprehensions
# links = [anchor["href"] for anchor in anchors]

# print(links)

###############
# step 8
###############

# link_content = requests.get("https://www.codefellows.org" + links[1])
# link_soup = BeautifulSoup(link_content.content, "html.parser")

# article = link_soup("article")[1]

# list_items = article.select("ul li ul li")

# print(titles[1].text)
# for li in list_items:
#     print(li.text)
